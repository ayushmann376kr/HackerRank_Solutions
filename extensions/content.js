chrome.runtime.onMessage.addListener(
    (request, sender, sendResponse) => {

        if (request.action === "getProblem") {

            // Get the page title
            const title = document.title;

            // Get the current URL
            const url = window.location.href;

            // Get all visible text
            const pageText = document.body.innerText;

            // Try to find the code editor
            let code = "";

            // Monaco editor
            const monacoLines = document.querySelectorAll(
                ".view-lines .view-line"
            );

            if (monacoLines.length > 0) {

                code = Array.from(monacoLines)
                    .map(line => line.innerText)
                    .join("\n");
            }

            // Try textarea editors as fallback
            if (!code) {

                const textarea = document.querySelector(
                    "textarea"
                );

                if (textarea) {
                    code = textarea.value;
                }
            }

            let language = "Unknown";

const pageLower = pageText.toLowerCase();

if (
    pageLower.includes("language: c++") ||
    code.includes("#include <iostream>") ||
    code.includes("using namespace std")
) {
    language = "C++";
}
else if (
    pageLower.includes("language: c") ||
    code.includes("#include <stdio.h>") ||
    code.includes("printf(")
) {
    language = "C";
}
else if (
    pageLower.includes("language: python") ||
    code.includes("def ") ||
    code.includes("print(")
) {
    language = "Python";
}
else if (
    pageLower.includes("language: java") ||
    code.includes("public static void main") ||
    code.includes("System.out")
) {
    language = "Java";
}
else if (
    pageLower.includes("language: javascript")
) {
    language = "JavaScript";
}
else if (
    pageLower.includes("language: typescript")
) {
    language = "TypeScript";
}
else if (
    pageLower.includes("language: sql")
) {
    language = "SQL";
}

            sendResponse({
                title: title,
                url: url,
                text: pageText,
                code: code,
                language: language
            });
        }

        return true;
    }
);