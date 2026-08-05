
(function(){
  function clock(){try{var d=new Date();var h=d.getHours(),m=d.getMinutes();var ap=h>=12?'PM':'AM';var hh=h%12;if(hh===0)hh=12;
    document.getElementById('clock').textContent=hh+':'+('0'+m).slice(-2)+' '+ap+' in India';}catch(e){}}
  clock();setInterval(clock,10000);
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var appWidth=innerWidth,appHeight=innerHeight;
  function syncViewport(){
    // Use the real page viewport. outerWidth/outerHeight describe the Chrome window frame
    // and previously made the pinned hero shorter than the visible screen.
    appWidth=document.documentElement.clientWidth||innerWidth;
    appHeight=(window.visualViewport&&visualViewport.height)||innerHeight;
    document.documentElement.style.setProperty('--app-width',Math.round(appWidth)+'px');
    document.documentElement.style.setProperty('--app-height',Math.round(appHeight)+'px');
  }
  syncViewport();
  var wrap=document.getElementById('pinwrap'),track=document.getElementById('track'),pin=wrap&&wrap.querySelector('.pin');
  function layoutPin(){if(!wrap||!track||!pin)return;
    var visibleW=document.documentElement.clientWidth,pinH=pin.getBoundingClientRect().height;
    var horizontalTravel=Math.max(0,track.scrollWidth-visibleW);
    // Give every still enough dwell time; the page cannot release until the full track has completed.
    var viewingTravel=horizontalTravel+pinH*.65;
    wrap.style.height=Math.ceil(pinH+viewingTravel)+'px';
    wrap.dataset.horizontalTravel=Math.round(horizontalTravel);
    wrap.dataset.viewingTravel=Math.round(viewingTravel);
  }
  layoutPin();requestAnimationFrame(function(){requestAnimationFrame(layoutPin);});addEventListener('load',layoutPin);
  if(window.ResizeObserver&&wrap&&track){new ResizeObserver(function(){layoutPin();}).observe(track);}
  var grads=[].slice.call(document.querySelectorAll('.grad'));
  function onScroll(){var rect=wrap.getBoundingClientRect();var pinH=pin?pin.getBoundingClientRect().height:innerHeight;
    var total=Math.max(1,wrap.offsetHeight-pinH);
    var p=Math.min(1,Math.max(0,(-rect.top)/total));var dist=Math.max(0,track.scrollWidth-document.documentElement.clientWidth);
    track.style.transform='translateX('+(-p*dist)+'px)';
    // three topic-change transitions: each runs once, in its own location
    grads.forEach(function(grad){var glow=grad.querySelector('.glow');if(!glow)return;
      var gr=grad.getBoundingClientRect(),gt=Math.max(1,grad.offsetHeight-appHeight);
      var gp=Math.min(1,Math.max(0,(-gr.top)/gt));
      // Exact reference rhythm: white → rising colour dome → black hold → rising inverse dome → white.
      var first=Math.min(1,Math.max(0,gp/.38));
      var second=Math.min(1,Math.max(0,(gp-.62)/.38));
      var firstEase=first*first*first*(first*(first*6-15)+10);
      var secondEase=second*second*second*(second*(second*6-15)+10);
      glow.style.opacity='1';
      glow.style.setProperty('--first-y',(82-82*firstEase).toFixed(2)+'%');
      glow.style.setProperty('--first-scale',(.42+3.18*firstEase).toFixed(3));
      glow.style.setProperty('--second-y',(82-82*secondEase).toFixed(2)+'%');
      glow.style.setProperty('--second-scale',(.42+3.18*secondEase).toFixed(3));
      var gtx=grad.querySelector('.gtext');if(gtx){
        var textIn=Math.min(1,Math.max(0,(gp-.24)/.14));
        var textOut=Math.min(1,Math.max(0,(.76-gp)/.14));
        gtx.style.opacity=(textIn*textOut).toFixed(3);
        gtx.style.color='#fff';
      }
    });
  }
  var scrollQueued=false;
  function scheduleScroll(){if(scrollQueued)return;scrollQueued=true;requestAnimationFrame(function(){scrollQueued=false;onScroll();});}
  addEventListener('scroll',scheduleScroll,{passive:true});addEventListener('resize',function(){syncViewport();layoutPin();onScroll();});onScroll();

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
    var A=[0,0,0],Bv=[0,0,0],stageW=0,stageH=0,compact=false;
    var SPD=[12,8,5.5];                // natural inner-to-outer orbital speeds
    var SIZE=[.84,.87,.90,.85,.89,.88,.83,.89,.85];
    var TILT=-7*Math.PI/180;
    var drag=0,vel=0,dragging=false,lastX=0,hover=false,t=0,last=null;
    function size(){
      stageW=stage.clientWidth;stageH=stage.clientHeight;
      var w=Math.min(stageW,1440),h=stageH;compact=stageW<600;
      if(compact){
        A[0]=w*.14;A[1]=w*.25;A[2]=w*.36;
        Bv[0]=h*.11;Bv[1]=h*.22;Bv[2]=h*.33;
      }else{
        A[0]=w*.17;A[1]=w*.30;A[2]=w*.425;
        Bv[0]=h*.12;Bv[1]=h*.255;Bv[2]=h*.365;
      }
      for(var i=0;i<3;i++){if(paths[i]){paths[i].style.width=(A[i]*2)+'px';paths[i].style.height=(Bv[i]*2)+'px';}}
    }
    function entryProgress(){
      if(reduce){entry=1;}else{var r=stage.getBoundingClientRect();var raw=(appHeight-r.top)/(appHeight*.78);raw=Math.min(1,Math.max(0,raw));entry=raw*raw*(3-2*raw);}
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
        var sc=perspective*(compact?.60:SIZE[i])*(.76+.24*entry);
        var pc=p.querySelector('.pc'),diam=pc?pc.offsetWidth:148;
        states.push({p:p,x:xr,y:yr,sc:sc,r:diam*sc*.5,depth:depth});
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
      if(r.bottom<-80||r.top>appHeight+80)return;
      var c=(r.top+r.height/2-appHeight/2)/appHeight;
      m.style.transform='translateY('+(c*-26).toFixed(1)+'px) scale(1.09)';});ticking=false;}
    addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(par);}},{passive:true});par();
  }
})();
