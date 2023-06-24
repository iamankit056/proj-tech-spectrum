// Start of Carousel code
var carousel = document.querySelector(".carousel");
var slides = carousel.querySelectorAll(".slide");
var activeSlide = carousel.querySelector("[data-active]");
console.log(slides)

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
  // const carousel = document.querySelector(".carousel");
  // const slides = carousel.arra.querySelectorAll(".slide");

  // // Set the slide interval in milliseconds
  // const slideInterval = 3000;

  // // Initialize the current slide index
  // let currentSlide = 0;

  // // Define a function to move to the next slide
  // function moveToNextSlide() {
  //   // Remove the data-active attribute from the current slide
  //   slides[currentSlide].removeAttribute("data-active");

  //   // Increment the current slide index or reset it to zero if it reaches the end
  //   currentSlide = (currentSlide + 1) % slides.length;

  //   // Add the data-active attribute to the next slide
  //   slides[currentSlide].setAttribute("data-active", "");

  //   // No need to update the transform property as the opacity will handle the fade effect
  // }

  // // Set an interval to call the moveToNextSlide function every slideInterval milliseconds
  // setInterval(moveToNextSlide, slideInterval);
// menu in same screen
function menu() {
  link = document.getElementById("link");
  if (link.style.display === "none") {
    link.style.display = "block";
  } else {
    link.style.display = "none";
  }
}
