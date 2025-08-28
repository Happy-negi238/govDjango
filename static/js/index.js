let blink = document.querySelector(".blink")

addEventListener("DOMContentLoaded", ()=>{
  // blink.style.backgroundColor="red";
  blink.style.animationName="blink-one"
})



const accordians = document.querySelectorAll(".accordian");

accordians.forEach(accor => {
    const icon = accor.querySelector('.icon');
    const answer = accor.querySelector('.answer');
    
    accor.addEventListener('click', () => {
        if(icon.classList.contains('active')){
            icon.classList.remove('active');
            answer.style.maxHeight = null;
        } else{
            icon.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + "px";
        }
    })
});



// start slider 


(() => {
  const slider = document.getElementById('slider1');
  const track  = slider.querySelector('.slider-track');
  const prev   = slider.querySelector('.prev');
  const next   = slider.querySelector('.next');

  const slides = Array.from(track.children);
  const firstClone = slides[0].cloneNode(true);
  const lastClone  = slides[slides.length - 1].cloneNode(true);
  track.insertBefore(lastClone, slides[0]);
  track.appendChild(firstClone);

  let index = 1;
  let slideWidth = slider.clientWidth;
  let isAnimating = false;
  let timer;

  function setTransform(animate = true) {
    track.style.transition = animate ? `transform var(--transition)` : 'none';
    track.style.transform = `translateX(${-index * slideWidth}px)`;
  }

  function go(n) {
    if (isAnimating) return;
    isAnimating = true;
    index += n;
    setTransform(true);
  }

  function handleTransitionEnd() {
    const allSlides = track.children;
    if (allSlides[index].isSameNode(firstClone)) {
      index = 1;
      setTransform(false);
    }
    if (allSlides[index].isSameNode(lastClone)) {
      index = slides.length;
      setTransform(false);
    }
    isAnimating = false;
  }

  track.addEventListener('transitionend', handleTransitionEnd);

  next.addEventListener('click', () => { stopAuto(); go(1); startAuto(); });
  prev.addEventListener('click', () => { stopAuto(); go(-1); startAuto(); });

  function startAuto() {
    timer = setInterval(() => go(1), 3000);
  }

  function stopAuto() {
    clearInterval(timer);
  }

  window.addEventListener('resize', () => {
    slideWidth = slider.clientWidth;
    setTransform(false);
  });

  setTransform(false);
  startAuto();
})();

// end slider