
(function(){
  function clock(){try{var d=new Date();var h=d.getHours(),m=d.getMinutes();var ap=h>=12?'PM':'AM';var hh=h%12;if(hh===0)hh=12;
    document.getElementById('clock').textContent=hh+':'+('0'+m).slice(-2)+' '+ap+' in India';}catch(e){}}
  clock();setInterval(clock,10000);
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var progress=document.createElement('div');progress.className='scroll-progress';document.body.appendChild(progress);
  var wrap=document.getElementById('pinwrap'),track=document.getElementById('track');
  var grads=[].slice.call(document.querySelectorAll('.grad'));
  function onScroll(){var rect=wrap.getBoundingClientRect();var total=wrap.offsetHeight-innerHeight;
    var p=Math.min(1,Math.max(0,(-rect.top)/total));var dist=track.scrollWidth-innerWidth;
    track.style.transform='translateX('+(-p*dist)+'px)';
    // three topic-change transitions: each runs once, in its own location
    grads.forEach(function(grad){var glow=grad.querySelector('.glow');if(!glow)return;
      var gr=grad.getBoundingClientRect(),gt=Math.max(1,grad.offsetHeight-innerHeight);
      var gp=Math.min(1,Math.max(0,(-gr.top)/gt));
      var o=gp<.20?(gp/.20):(gp>.84?(1-(gp-.84)/.16):1);
      o=Math.min(1,Math.max(0,o));
      var sm=(o*o*(3-2*o)).toFixed(3);glow.style.opacity=sm;
      var gtx=grad.querySelector('.gtext');if(gtx){gtx.style.opacity=sm;gtx.style.color=gp<.62?'#ffffff':'#171717';}
    });
    var doc=document.documentElement,den=Math.max(1,doc.scrollHeight-innerHeight);
    progress.style.transform='scaleX('+Math.min(1,Math.max(0,scrollY/den)).toFixed(4)+')';}
  addEventListener('scroll',onScroll,{passive:true});addEventListener('resize',onScroll);onScroll();
  // ensure videos play (autoplay fallback)
  document.querySelectorAll('video').forEach(function(v){v.muted=true;var pr=v.play();if(pr&&pr.catch)pr.catch(function(){});});
  // index hover thumb follows cursor
  if(matchMedia('(hover:hover)').matches){
    document.querySelectorAll('#index .row').forEach(function(row){var th=row.querySelector('.thumb');
      row.addEventListener('mouseenter',function(){row.classList.add('show');});
      row.addEventListener('mouseleave',function(){row.classList.remove('show');});
      row.addEventListener('mousemove',function(e){if(th){th.style.left=e.clientX+'px';th.style.top=e.clientY+'px';}});
    });
  }

  // brand solar system: studio sun + orbiting brand planets, drag to spin
  (function(){
    var stage=document.getElementById('solar');if(!stage)return;
    var planets=[].slice.call(stage.querySelectorAll('.planet'));
    var paths=[].slice.call(stage.querySelectorAll('.opath'));
    var ghost=stage.querySelector('.ghost'),wordmark=stage.querySelector('.sun');
    var entry=reduce?1:0;
    var A=[0,0,0],Bv=[0,0,0],stageW=0,stageH=0;
    var SPD=[17,10,5.5];               // calm inner-to-outer orbit speeds
    var SIZE=[.72,.78,.84,.74,.80,.82,.72,.81,.75]; // controlled depth without oversized collisions
    var TILT=-7*Math.PI/180;
    var drag=0,vel=0,dragging=false,lastX=0,hover=false,t=0,last=null;
    function size(){
      stageW=stage.clientWidth;stageH=stage.clientHeight;
      var w=Math.min(stageW,1440),h=stageH;
      A[0]=w*0.14;A[1]=w*0.26;A[2]=w*0.38;
      Bv[0]=h*0.10;Bv[1]=h*0.225;Bv[2]=h*0.35;
      for(var i=0;i<3;i++){if(paths[i]){paths[i].style.width=(A[i]*2)+'px';paths[i].style.height=(Bv[i]*2)+'px';}}
    }
    function entryProgress(){
      if(reduce){entry=1;}else{var r=stage.getBoundingClientRect();var raw=(innerHeight-r.top)/(innerHeight*.78);raw=Math.min(1,Math.max(0,raw));entry=raw*raw*(3-2*raw);}
      if(ghost){ghost.style.opacity=(.28+.72*entry).toFixed(3);ghost.style.transform='translateY(-50%) scaleX('+(.84+.07*entry).toFixed(3)+')';ghost.style.letterSpacing=(-.02-.055*entry).toFixed(3)+'em';}
      if(wordmark){wordmark.style.opacity=(.25+.75*entry).toFixed(3);wordmark.style.transform='translate(-50%,-50%) scale('+(.78+.22*entry).toFixed(3)+')';}
    }
    size();entryProgress();addEventListener('resize',function(){size();entryProgress();});addEventListener('scroll',entryProgress,{passive:true});
    stage.addEventListener('mouseenter',function(){hover=true;});
    stage.addEventListener('mouseleave',function(){hover=false;});
    stage.addEventListener('pointerdown',function(e){dragging=true;lastX=e.clientX;vel=0;stage.classList.add('grabbing');e.preventDefault();});
    addEventListener('pointermove',function(e){if(!dragging)return;var d=(e.clientX-lastX)*0.4;lastX=e.clientX;drag+=d;vel=d;});
    addEventListener('pointerup',function(){dragging=false;stage.classList.remove('grabbing');});
    function frame(now){
      if(last==null)last=now;var dt=Math.min(0.05,(now-last)/1000);last=now;
      if(!reduce){
        if(!dragging){
          if(Math.abs(vel)>0.06){drag+=vel;vel*=0.955;}
        }
        t+=dt*(hover?0.5:1);
      }
      var states=[];
      for(var i=0;i<planets.length;i++){
        var p=planets[i],o=+p.getAttribute('data-o'),off=+p.getAttribute('data-off');
        var th=((reduce?0:SPD[o]*t)+off+drag)*Math.PI/180;
        var x=A[o]*Math.cos(th),y=Bv[o]*Math.sin(th);
        var xr=(x*Math.cos(TILT)-y*Math.sin(TILT)),yr=(x*Math.sin(TILT)+y*Math.cos(TILT));
        var depth=Math.sin(th),perspective=.82+.28*((depth+1)/2);
        var reveal=.18+.82*entry;xr*=reveal;yr*=reveal;
        var sc=perspective*SIZE[i]*(.76+.24*entry);
        var pc=p.querySelector('.pc'),diam=pc?pc.offsetWidth:148;
        states.push({p:p,x:xr,y:yr,sc:sc,r:diam*sc*.5,depth:depth});
      }
      // Reserve a clean zone around AITEIT, then resolve sphere-to-sphere collisions.
      for(var c=0;c<states.length;c++){
        var s=states[c],d=Math.sqrt(s.x*s.x+s.y*s.y)||.001,min=(98+s.r)*(.38+.62*entry);
        if(d<min){var push=min-d;s.x+=s.x/d*push;s.y+=s.y/d*push;}
      }
      for(var pass=0;pass<5;pass++)for(var a=0;a<states.length;a++)for(var b=a+1;b<states.length;b++){
        var one=states[a],two=states[b],dx=two.x-one.x,dy=two.y-one.y,dist=Math.sqrt(dx*dx+dy*dy);
        var gap=(one.r+two.r+16)*(.35+.65*entry);
        if(dist<gap){if(dist<.001){dx=Math.cos((a+1)*(b+2));dy=Math.sin((a+1)*(b+2));dist=1;}
          var move=(gap-dist)*.5,nx=dx/dist,ny=dy/dist;
          one.x-=nx*move;one.y-=ny*move;two.x+=nx*move;two.y+=ny*move;}
      }
      for(var q=0;q<states.length;q++){
        var st=states[q],maxX=Math.max(40,stageW*.5-st.r-28),maxY=Math.max(40,stageH*.5-st.r-54);
        st.x=Math.max(-maxX,Math.min(maxX,st.x));st.y=Math.max(-maxY,Math.min(maxY,st.y));
        st.p.style.transform='translate(calc(-50% + '+st.x.toFixed(1)+'px),calc(-50% + '+st.y.toFixed(1)+'px)) scale('+st.sc.toFixed(3)+')';
        st.p.style.zIndex=String(Math.round(50+st.depth*40));
        st.p.style.opacity=((0.76+0.24*((st.depth+1)/2))*entry).toFixed(3);
        st.p.style.filter='brightness('+(0.96+0.04*((st.depth+1)/2)).toFixed(3)+') saturate('+(1.00+0.08*((st.depth+1)/2)).toFixed(3)+')';
      }
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  })();

  // scroll reveals (staggered, professional)
  var revEls=[].slice.call(document.querySelectorAll('.vexp .panel,.index .row,.arch .a,.seclbl,.statement h2,.about p,.chron .row'));
  if(reduce){revEls.forEach(function(el){el.classList.add('in');});}
  else{
    var stagger={'.index .row':0,'.arch .a':0};
    var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
      var el=e.target,d=0;
      if(el.matches('.index .row'))d=(Array.prototype.indexOf.call(el.parentNode.children,el)%6)*55;
      if(el.matches('.arch .a'))d=(Array.prototype.indexOf.call(el.parentNode.children,el)%6)*45;
      setTimeout(function(){el.classList.add('in');},d);
      ro.unobserve(el);}});},{threshold:.15});
    revEls.forEach(function(el){ro.observe(el);});
  }

  // videos: play only near viewport (perf) + gentle parallax on panel media
  var vids=[].slice.call(document.querySelectorAll('video'));
  var vo=new IntersectionObserver(function(es){es.forEach(function(e){
    var v=e.target;if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){});}else{v.pause();}
  });},{rootMargin:'240px 0px'});
  vids.forEach(function(v){vo.observe(v);});
  if(!reduce){
    var medias=[].slice.call(document.querySelectorAll('.vexp .panel .media video'));
    var ticking=false;
    function par(){medias.forEach(function(m){var r=m.getBoundingClientRect();
      if(r.bottom<-80||r.top>innerHeight+80)return;
      var c=(r.top+r.height/2-innerHeight/2)/innerHeight;
      m.style.transform='translateY('+(c*-26).toFixed(1)+'px) scale(1.09)';});ticking=false;}
    addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(par);}},{passive:true});par();
  }
})();
