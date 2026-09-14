document
    .getElementById("saveButton")
    .addEventListener("click", async () => {

        const status = document.getElementById("status");

        status.innerText = "Reading HackerRank...";

        try {

            const tabs = await chrome.tabs.query({
                active: true,
                currentWindow: true
            });

            const tab = tabs[0];

            const response = await chrome.tabs.sendMessage(
                tab.id,
                {
                    action: "getProblem"
                }
            );

            console.log(response);

            status.innerText = "Sending to Python...";

            const serverResponse = await fetch(
                "http://127.0.0.1:5000/save",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(response)
                }
            );

            const result = await serverResponse.json();

            console.log(result);

            status.innerText =
                "Successfully sent to Python!";

        } catch (error) {

            console.error(error);

            status.innerText =
                "Something went wrong.";

        }

    });