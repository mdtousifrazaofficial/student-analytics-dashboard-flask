// ===============================
// STUDENT MANAGEMENT SYSTEM
// app.js
// ===============================

console.log(
    "Student Management System Loaded"
);

// ===============================
// DELETE CONFIRMATION
// ===============================

const deleteButtons = document.querySelectorAll(
    ".btn-danger"
);

deleteButtons.forEach((button) => {

    button.addEventListener("click", function (event) {

        const confirmDelete = confirm(
            "Are you sure you want to delete this student?"
        );

        if (!confirmDelete) {

            event.preventDefault();
        }
    });
});

// ===============================
// FORM VALIDATION
// ===============================

const studentForm = document.querySelector(
    ".student-form"
);

if (studentForm) {

    studentForm.addEventListener(
        "submit",
        function (event) {

            const inputs = studentForm.querySelectorAll(
                "input"
            );

            let valid = true;

            inputs.forEach((input) => {

                if (input.value.trim() === "") {

                    valid = false;

                    input.style.border =
                        "2px solid red";

                } else {

                    input.style.border =
                        "1px solid rgba(255,255,255,0.08)";
                }
            });

            // MARKS VALIDATION

            const subject1 = parseInt(
                document.querySelector(
                    'input[name="subject1"]'
                ).value
            );

            const subject2 = parseInt(
                document.querySelector(
                    'input[name="subject2"]'
                ).value
            );

            const subject3 = parseInt(
                document.querySelector(
                    'input[name="subject3"]'
                ).value
            );

            if (
                subject1 > 100 ||
                subject2 > 100 ||
                subject3 > 100
            ) {

                alert(
                    "Marks cannot be greater than 100"
                );

                valid = false;
            }

            if (
                subject1 < 0 ||
                subject2 < 0 ||
                subject3 < 0
            ) {

                alert(
                    "Marks cannot be negative"
                );

                valid = false;
            }

            if (!valid) {

                event.preventDefault();

                alert(
                    "Please fill all fields correctly."
                );
            }
        }
    );
}

// ===============================
// SEARCH BAR EFFECT
// ===============================

const searchInput = document.querySelector(
    '.search-box input'
);

if (searchInput) {

    searchInput.addEventListener(
        "focus",
        () => {

            searchInput.style.boxShadow =
                "0 0 15px rgba(59,130,246,0.5)";
        }
    );

    searchInput.addEventListener(
        "blur",
        () => {

            searchInput.style.boxShadow = "none";
        }
    );
}

// ===============================
// TABLE ROW ANIMATION
// ===============================

const tableRows = document.querySelectorAll(
    "tbody tr"
);

tableRows.forEach((row, index) => {

    row.style.opacity = "0";

    row.style.transform = "translateY(20px)";

    setTimeout(() => {

        row.style.transition =
            "all 0.5s ease";

        row.style.opacity = "1";

        row.style.transform =
            "translateY(0)";

    }, index * 120);
});

// ===============================
// WELCOME MESSAGE
// ===============================

window.addEventListener("load", () => {

    console.log(
        "Welcome To Student Dashboard"
    );
});

// ===============================
// LIVE CLOCK
// ===============================

const subtitle = document.querySelector(
    ".subtitle"
);

function updateClock() {

    const now = new Date();

    const time = now.toLocaleTimeString();

    if (subtitle) {

        subtitle.innerHTML =
            `Manage students professionally • ${time}`;
    }
}

setInterval(updateClock, 1000);
