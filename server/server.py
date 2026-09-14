from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import re
import subprocess


app = Flask(__name__)

CORS(app)


# --------------------------------------------------
# Convert problem name into a safe folder name
# --------------------------------------------------

def slugify(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9]+",
        "-",
        text
    )

    return text.strip("-")


# --------------------------------------------------
# Get correct file extension
# --------------------------------------------------

def get_extension(language):

    extensions = {

        "C": ".c",

        "C++": ".cpp",

        "Python": ".py",

        "Java": ".java",

        "JavaScript": ".js",

        "TypeScript": ".ts",

        "SQL": ".sql"

    }

    return extensions.get(
        language,
        ".txt"
    )


# --------------------------------------------------
# Save HackerRank problem
# --------------------------------------------------

@app.route("/save", methods=["POST"])
def save_solution():

    try:

        data = request.json

        title = data.get(
            "title",
            "Unknown Problem"
        )

        url = data.get(
            "url",
            ""
        )

        text = data.get(
            "text",
            ""
        )

        code = data.get(
            "code",
            ""
        )

        language = data.get(
            "language",
            "Unknown"
        )


        print("\n==============================")
        print("HackerRank Problem Received")
        print("==============================")

        print("Title:", title)
        print("Language:", language)
        print("URL:", url)

        print("\nCode:")
        print(code)


        # ------------------------------------------
        # Remove HackerRank title suffix
        # ------------------------------------------

        problem_name = title

        if " | HackerRank" in problem_name:

            problem_name = problem_name.replace(
                " | HackerRank",
                ""
            )


        # ------------------------------------------
        # Create folder
        # ------------------------------------------

        language_folder = language

        problem_folder = slugify(
            problem_name
        )


        folder_path = os.path.join(
            language_folder,
            problem_folder
        )


        os.makedirs(
            folder_path,
            exist_ok=True
        )


        # ------------------------------------------
        # Create question.md
        # ------------------------------------------

        question_file = os.path.join(
            folder_path,
            "question.md"
        )


        question_content = f"""# {problem_name}

## HackerRank

{url}

## Language

{language}

## Problem Statement

{text}

"""


        with open(
            question_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                question_content
            )


        # ------------------------------------------
        # Create solution file
        # ------------------------------------------

        extension = get_extension(
            language
        )


        solution_file = os.path.join(
            folder_path,
            "solution" + extension
        )


        with open(
            solution_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                code
            )


        print("\nFiles created:")

        print(
            question_file
        )

        print(
            solution_file
        )


        # ------------------------------------------
        # Git add
        # ------------------------------------------

        subprocess.run(
            ["git", "add", "."],
            check=True
        )


        # ------------------------------------------
        # Git commit
        # ------------------------------------------

        commit_message = (
            f"Solve HackerRank: {problem_name}"
        )


        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                commit_message
            ],
            check=True
        )


        # ------------------------------------------
        # Git push
        # ------------------------------------------

        subprocess.run(
            ["git", "push"],
            check=True
        )


        print("\nSuccessfully pushed to GitHub!")


        return jsonify({

            "success": True,

            "message":
                "Problem successfully pushed to GitHub.",

            "folder":
                folder_path

        })


    except subprocess.CalledProcessError as error:

        print(
            "\nGit error:",
            error
        )

        return jsonify({

            "success": False,

            "message":
                "Git command failed. Check the terminal."

        }), 500


    except Exception as error:

        print(
            "\nError:",
            error
        )

        return jsonify({

            "success": False,

            "message":
                str(error)

        }), 500


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.route("/")
def home():

    return (
        "HackerRank GitHub Server "
        "is running!"
    )


# --------------------------------------------------
# Start server
# --------------------------------------------------

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )