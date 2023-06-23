// Start of Carousel code
var carousel = document.querySelector(".carousel");
var slides = carousel.querySelectorAll(".slide");
var activeSlide = carousel.querySelector("[data-active]");

var activeIndex = Array.prototype.indexOf.call(slides, activeSlide);
function nextSlide() {
  activeSlide.removeAttribute("data-active");
  activeIndex++;
  if (activeIndex == slides.length) {
    activeIndex = 0;
  }
  activeSlide = slides[activeIndex];
  activeSlide.setAttribute("data-active", "");
}

function prevSlide() {
  activeSlide.removeAttribute("data-active");
  activeIndex--;
  if (activeIndex < 0) {
    activeIndex = slides.length - 1;
  }
  activeSlide = slides[activeIndex];
  activeSlide.setAttribute("data-active", "");
}

var interval = setInterval(nextSlide, 3000);
document.addEventListener("keydown", function (event) {
  if (event.keyCode == 37) {
    prevSlide();
    clearInterval(interval);
    interval = setInterval(nextSlide, 3000);
  }

  if (event.keyCode == 39) {
    nextSlide();
    clearInterval(interval);
    interval = setInterval(nextSlide, 3000);
  }
});
//end of carousel code

//menu in same screen
