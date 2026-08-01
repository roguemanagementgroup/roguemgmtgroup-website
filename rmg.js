
(function(){
var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* scroll rail */
var rail=document.getElementById("rail");
addEventListener("scroll",function(){
  var h=document.documentElement;
  rail.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+"%";
},{passive:true});

/* reveals */
var io=new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting) return;
    e.target.classList.add("in");
    if(e.target.classList.contains("nums")||e.target.classList.contains("num")) count(e.target);
    io.unobserve(e.target);
  });
},{threshold:.15,rootMargin:"0px 0px -60px 0px"});
document.querySelectorAll(".rv,.wipe,.permit").forEach(function(n){ io.observe(n); });

/* counters */
function count(scope){
  scope.querySelectorAll("i[data-to]").forEach(function(el){
    var to=+el.dataset.to, t0=performance.now(), dur=1400;
    if(reduce||to===0){ el.textContent=to.toLocaleString(); return; }
    (function step(t){
      var p=Math.min((t-t0)/dur,1), e=1-Math.pow(1-p,3);
      el.textContent=Math.round(to*e).toLocaleString();
      if(p<1) requestAnimationFrame(step);
    })(t0);
  });
}

/* flag: drifting star field with an assembling canton */
if(!reduce){
  var c=document.getElementById("flag"), x=c.getContext("2d"), drift=[], canton=[], t=0;
  function star(cx,cy,r,rot){
    x.beginPath();
    for(var i=0;i<10;i++){
      var rad=(i%2?r*.42:r), a=Math.PI/5*i-Math.PI/2+rot;
      x[i?"lineTo":"moveTo"](cx+Math.cos(a)*rad, cy+Math.sin(a)*rad);
    }
    x.closePath(); x.fill();
  }
  function build(){
    var d=devicePixelRatio||1;
    c.width=innerWidth*d; c.height=innerHeight*d;
    drift=Array.from({length:260},function(){return{
      x:Math.random()*c.width,y:Math.random()*c.height,
      r:Math.random()*1.3+.2,s:Math.random()*.13+.03,a:Math.random()*.55+.15};});
    canton=[];
    var w=c.width, gx=w*.055, gy=c.height*.075, step=Math.min(w*.021,26*d);
    for(var row=0;row<9;row++){
      var n=row%2?5:6, off=row%2?step:0;
      for(var col=0;col<n;col++){
        canton.push({x:w-gx-(5-col)*step*2-off, y:gy+row*step*1.35, r:step*.34, d:(row*6+col)*26});
      }
    }
    canton=canton.slice(0,50);
  }
  function loop(now){
    x.clearRect(0,0,c.width,c.height);
    for(var i=0;i<drift.length;i++){
      var s=drift[i]; s.y-=s.s; if(s.y<0) s.y=c.height;
      x.globalAlpha=s.a; x.fillStyle="#e8e4da";
      x.beginPath(); x.arc(s.x,s.y,s.r,0,6.2832); x.fill();
    }
    for(var j=0;j<canton.length;j++){
      var k=canton[j], p=Math.min(Math.max((now-k.d)/900,0),1);
      if(p<=0) continue;
      var e=1-Math.pow(1-p,3);
      x.globalAlpha=.30*e; x.fillStyle="#e8e4da";
      star(k.x, k.y-(1-e)*22, k.r*e, (1-e)*1.1);
    }
    x.globalAlpha=1;
    requestAnimationFrame(loop);
  }
  build(); addEventListener("resize",build); requestAnimationFrame(loop);
}
})();
