/* Slide navbar links */

const navSlide = () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".navLinks");
  let clicks = 0;

  burger.onclick = () => {
    clicks += 1;
    if (clicks % 2 == 1) {
      nav.style.cssText =
        "transform: translateX(0%); transition: transform 0.5s ease-in;";
    }
    if (clicks > 0 && clicks % 2 == 0) {
      nav.style.cssText =
        "transform: translateX(100%); transition: transform 0.5s ease-in;";
    }
  };
};

/* Close alerts */
const closeAlerts = () => {
  const closeButtons = document.querySelectorAll(".close-alert");

  for (let closeButton of closeButtons) {
    closeButton.onclick = (e) => {
      e.target.parentNode.remove();
    };
  }
};

const app = () => {
  navSlide();
  closeAlerts();
};

app();
