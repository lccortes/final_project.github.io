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

  

  // Hide the chase animation after it's finished (7s after page load)
  window.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
      const wrapper = document.querySelector(".chase-wrapper");
      wrapper.classList.add("hide");
    }, 7000); // matches animation length
  });

  window.addEventListener("scroll", () => {
    const chart = document.getElementById("sankeyDiagram");
    const chartTop = chart.getBoundingClientRect().top;
    if (chartTop < window.innerHeight * 0.9) {
      chart.classList.add("animated");
    }
  });
  