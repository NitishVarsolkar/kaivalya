document.addEventListener("DOMContentLoaded", () => {
    const messages = document.getElementById("chatMessages");
    const userInput = document.getElementById("userInput");
    
    let step = 0;
    let userName = "";
    let dob = "";
    let tob = "";
    let place = "";

    function appendMessage(content, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = content;
        messages.appendChild(messageDiv);
        messages.scrollTop = messages.scrollHeight;
    }

    function handleBotResponse(input) {
        if (step === 0) {
            appendMessage("Hey there curious one, what brings you here today?", "bot");
            step++;
        } else if (step === 1) {
            appendMessage("Sure thing! To start with the procedure, please enter your name for me.", "bot");
            step++;
        } else if (step === 2) {
            userName = input;
            appendMessage(`Oh hey ${userName}, when were you born?`, "bot");
            step++;
        } else if (step === 3) {
            dob = input;
            appendMessage("Oh great! At what time?", "bot");
            step++;
        } else if (step === 4) {
            tob = input;
            appendMessage("Okay, and where exactly were you born?", "bot");
            step++;
        } else if (step === 5) {
            place = input;
            appendMessage("Sure thing! That'd be all. Here's your kundali...", "bot");

            setTimeout(() => {
                appendMessage("Loading...", "bot");
                setTimeout(() => {
                    appendMessage("🔮 [Kundali image generated here]", "bot");
                }, 2000);
            }, 1000);

            step++;
        } else {
            appendMessage("I've already got all the information I need. 😊", "bot");
        }
    }

    function sendMessage() {
        const input = userInput.value.trim();
        if (!input) return;

        appendMessage(input, "user");
        userInput.value = "";
        setTimeout(() => {
            handleBotResponse(input);
        }, 500);
    }

    document.querySelector("button").addEventListener("click", sendMessage);

    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
});
