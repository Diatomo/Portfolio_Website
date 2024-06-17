
const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll(".navigation-item");
const home = document.getElementById('home');
const navHome = document.getElementById('nav-home');

var prevCurrent = "";

window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;

    const OFFSET = 50;
    if (pageYOffset > sectionTop - OFFSET) {
        current = section.getAttribute("id");
    }
  });

    if (prevCurrent != current) {
        //alias
        prevCurrent = current;

        // loop through nav-bar list
        navLi.forEach((li) => {

            const classActiveName = "navigation-item--active";
            li.classList.remove(classActiveName);
            const currentElement = document.getElementById("nav-" + current)

            if (currentElement != null) {
                currentElement.classList.add(classActiveName);
            }
            else {
                navHome.classList.add(classActiveName);
            }

        });
    };
});



document.getElementById('form-submit').addEventListener('click', function(event){
    const form = document.getElementById('contact_form-1');
    if (validateForm()){
        form.requestSubmit()
        form.reset()
    }

    function validateForm() {

        var validated = true;
        // Validate Name
        var name = document.getElementById("contact_form-name-1").value;
        var name_error = document.getElementById("form_error-name-1");
        if (name == "" || name == null) {
            validated = false;
            name_error.style.display = 'block';
        } else {
            name_error.style.display = 'none';
        }

        // Validate Email
        var email = document.getElementById("contact_form-email-1").value;
        var email_error = document.getElementById("form_error-email-1");
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!regex.test(email) || email == "" || email == null) {
            validated = false;
            email_error.style.display = 'block';
        } else {
            email_error.style.display = 'none';
        }

        // Validate Message
        var message = document.getElementById("contact_form-message-1").value;
        var message_error = document.getElementById("form_error-message-1");
        if (message=="" || message==null) {
            validated=false;
            message_error.style.display = 'block';
        } else {
            message_error.style.display = 'none';
        }
        return validated;
    }

})


// Wait for the canvas to be created and then add a class to it
window.addEventListener('load', function() {
    var canvas = document.querySelector('#particles-js-1 > canvas');
    if (canvas) {
        canvas.classList.add('home-canvas');
    }
});


// Wait for the canvas to be created and then add a class to it
window.addEventListener('load', function() {
    var canvas = document.querySelector('#particles-js-2 > canvas');
    if (canvas) {
        canvas.classList.add('bg-canvas');
    }
});
