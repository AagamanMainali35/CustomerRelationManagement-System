
    // JavaScript to hide info alerts after 10 seconds
    document.addEventListener('DOMContentLoaded', function() {
      const alerts = document.querySelectorAll('.info-alert');
      alerts.forEach(alert => {
        setTimeout(() => {
          alert.style.opacity = '0';
          setTimeout(() => alert.remove(), 500); // Remove after transition
        }, 2000); // 10000 milliseconds = 10 seconds
      });
    });
