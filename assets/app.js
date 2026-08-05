
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
    track.style.transform='translate3d('+(-p*dist)+'px,0,0)';
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

  // Complete Drive-backed motion library. Posters are lazy; masters load on click.
  (function(){
    var grid=document.getElementById('motion-grid'),filters=document.getElementById('motion-filters');
    var count=document.getElementById('motion-count'),more=document.getElementById('motion-more');
    if(!grid||!filters||!count||!more)return;
    var state={items:[],filter:'All',expanded:false};
    function make(tag,cls,text){var el=document.createElement(tag);if(cls)el.className=cls;if(text!=null)el.textContent=text;return el;}
    function play(card,item){
      if(card.classList.contains('playing'))return;
      var launch=card.querySelector('.motion-launch');if(!launch)return;
      var video=document.createElement('video');video.src=(item.video.startsWith('http')?item.video:'https://aiteitai-growth.187-127-167-128.sslip.io:8443/website-preview/'+item.video);video.poster=item.poster;video.controls=true;video.autoplay=true;
      video.playsInline=true;video.preload='auto';video.setAttribute('aria-label',item.title);
      launch.replaceWith(video);card.classList.add('playing');var result=video.play();if(result&&result.catch)result.catch(function(){});
    }
    function render(){
      grid.textContent='';
      var list=state.items.filter(function(item){return state.filter==='All'||item.category===state.filter;});
      var visible=state.expanded?list:list.slice(0,12);
      visible.forEach(function(item){
        var card=make('article','motion-card');
        var launch=make('button','motion-launch');launch.type='button';launch.setAttribute('aria-label','Play '+item.title);
        launch.style.aspectRatio=item.width+' / '+item.height;
        var img=document.createElement('img');img.src=item.poster;img.alt='Poster frame from '+item.title;img.loading='lazy';img.decoding='async';
        img.width=item.width;img.height=item.height;
        var mark=make('span','playmark','PLAY');
        var meta=make('span','motion-meta');meta.append(make('span','motion-title',item.title),make('span','motion-cat',item.category));
        launch.append(img,mark,meta);card.append(launch);launch.addEventListener('click',function(){play(card,item);});grid.append(card);
      });
      count.textContent=visible.length+' of '+list.length+' projects';
      more.hidden=list.length<=12;more.textContent=state.expanded?'Show less':'Show the full library';
    }
    function setFilter(value){state.filter=value;state.expanded=false;[].slice.call(filters.children).forEach(function(b){
      var active=b.getAttribute('data-filter')===value;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});render();}
    fetch('media/web-video-catalog.json').then(function(response){if(!response.ok)throw new Error('catalog '+response.status);return response.json();}).then(function(items){
      state.items=items.filter(function(item){return !item.shelf_hidden;});var categories=['All'].concat(Array.from(new Set(state.items.map(function(item){return item.category;}))));
      categories.forEach(function(category){var button=make('button','motion-filter',category);button.type='button';button.setAttribute('data-filter',category);button.addEventListener('click',function(){setFilter(category);});filters.append(button);});
      more.addEventListener('click',function(){state.expanded=!state.expanded;render();});setFilter('All');
    }).catch(function(error){count.textContent='Library unavailable';grid.append(make('p','motion-error','The motion catalog could not load. Please use the full portfolio link below.'));console.error(error);});
  })();
  // project inquiry: qualify the brief, persist it through the private API, and return a reference.
  (function(){
    var form=document.getElementById('inquiry-form');if(!form)return;
    var status=document.getElementById('inquiry-status'),button=form.querySelector('.form-submit');
    var startedAt=Date.now();
    function show(kind,title,body){
      status.className='form-status show '+kind;status.textContent='';
      var strong=document.createElement('strong');strong.textContent=title;status.append(strong,document.createTextNode(body));
    }
    function clearErrors(){[].slice.call(form.querySelectorAll('.field.invalid')).forEach(function(field){field.classList.remove('invalid');});}
    [].slice.call(form.elements).forEach(function(input){input.addEventListener('input',function(){var field=input.closest('.field');if(field)field.classList.remove('invalid');});});
    form.addEventListener('submit',function(event){
      event.preventDefault();clearErrors();status.className='form-status';status.textContent='';
      if(!form.checkValidity()){
        var invalid=form.querySelector(':invalid');if(invalid){var field=invalid.closest('.field');if(field)field.classList.add('invalid');invalid.focus();}
        show('error','A few details are missing.',' Check the highlighted field and try again.');return;
      }
      var data=new FormData(form),payload={};data.forEach(function(value,key){payload[key]=value;});
      payload.started_at=startedAt;payload.source=location.href;payload.referrer=document.referrer;
      button.disabled=true;button.textContent='Sending…';
      fetch('api/project-inquiries',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
        .then(function(response){return response.json().catch(function(){return {error:'Unexpected response.'};}).then(function(body){if(!response.ok){var error=new Error(body.error||'Could not send this inquiry.');error.field=body.field;throw error;}return body;});})
        .then(function(body){
          form.reset();startedAt=Date.now();show('success','Brief received.',' Reference '+body.id+'. We will review the scope and reply to the email above, usually within two business days.');
        })
        .catch(function(error){
          if(error.field){var input=form.elements[error.field];if(input){var field=input.closest('.field');if(field)field.classList.add('invalid');input.focus();}}
          show('error','The brief was not sent.',' '+error.message+' You can also email weaiteit@gmail.com.');
        })
        .finally(function(){button.disabled=false;button.textContent='Send project brief →';});
    });
  })();
