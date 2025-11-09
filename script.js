let count = 0;

const greetBtn = document.getElementById("greetBtn");
const nameInput = document.getElementById("nameInput");
const output = document.getElementById("output");
const countDisplay = document.getElementById("count");

// If the DOM elements are not yet available when this file loads,
// attach the listener after DOMContentLoaded.
function setup() {
    if (!greetBtn || !nameInput || !output || !countDisplay) return;

    greetBtn.addEventListener("click", function() {
        const name = nameInput.value.trim();

        count++;

        if (name === "") {
            output.innerText = "Please enter your name!";
            output.style.color = "red";
        } else {
            output.innerText = "Hello " + name + "!";
            output.style.color = "green";
            document.body.style.backgroundColor =
                document.body.style.backgroundColor === "lightyellow" ?
                "#eef6ff" :
                "lightyellow"; // toggle background color
        }

        countDisplay.innerText = "Button clicks: " + count;
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup);
} else {
    setup();
}