let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick =() => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll =() =>{
     menu.classList.remove('bx-x');
     navbar.classList.remove('active');
}

// Close menu when clicking on navbar links
document.querySelectorAll('.navbar a').forEach(link => {
    link.onclick = () => {
        menu.classList.remove('bx-x');
        navbar.classList.remove('active');
    }
})
const sr = ScrollReveal({
    distance:'10px',
    duration: 2500,
    delay:400,
    reset:true
})

sr.reveal('.text',{delay:200, origin:'top'})
sr.reveal('.form-container form',{delay:800, origin:'left'})
sr.reveal('.heading',{delay:800, origin:'top'})
sr.reveal('.ride-container .box',{delay:600, origin:'top'})
sr.reveal('.services-container .box',{delay:600, origin:'top'}) 
sr.reveal('.about-text',{delay:600, origin:'top'})
sr.reveal('.newsletter .box',{delay:400, origin:'bottom'})

// Toggle more text in about section (safer: toggle class)
const learnMoreBtn = document.querySelector('.about-text .btn');
const moreText = document.querySelector('.more-text');

learnMoreBtn.addEventListener('click', (e) => {
    e.preventDefault();
    if (moreText.style.display === 'none' || moreText.style.display === '') {
        moreText.style.display = 'block';
        learnMoreBtn.textContent = 'Show Less';
    } else {
        moreText.style.display = 'none';
        learnMoreBtn.textContent = 'Learn More';
    }
});

// Dropdown for login/logout (guarded: only attach handlers if element exists)
const userMenu = document.querySelector('.user-menu');
if (userMenu) {
    userMenu.addEventListener('click', (e) => {
        e.stopPropagation();
        userMenu.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!userMenu.contains(e.target)) {
            userMenu.classList.remove('active');
        }
    });
}

// Choose City Modal Functions
function openCityModal() {
    document.getElementById("cityModal").style.display = "block";
}

function closeCityModal() {
    document.getElementById("cityModal").style.display = "none";
}

/* Close modal on outside click */
window.addEventListener('click', function(event) {
    let modal = document.getElementById("cityModal");
    if (modal && event.target === modal) {
        modal.style.display = "none";
    }
});