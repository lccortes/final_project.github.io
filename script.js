// Add smooth scrolling to anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });
  
  window.addEventListener("scroll", () => {
    const scrollPos = window.scrollY + window.innerHeight;
    const docHeight = document.documentElement.offsetHeight;
    const partyZone = document.getElementById("bike-party");
  
    if (scrollPos >= docHeight - 10) {
      partyZone.classList.add("show");
    }
  });
  
  