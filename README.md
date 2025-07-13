# My Okada Hackathon Project

Thank you for taking the time to look at my project. Sadly, I could not do most of what I wanted to do within the deadline, as Python is not my strong suit and learning to integrate AI into my work is a very new concept for me. However, despite this being a work-in-progress project, I have certainly made some positive developments and have managed to successfully send context to Groq AI for an educated response. Regardless of how I rank when being judged amongst other contestants, I would say this has certainly been a learning experience.

## Before Using My Project

Just as a small disclaimer, there is a script in here that I used to convert the mockup .csv file into chunks. There is no need to run the script again, but I left it there just to show the process. The script first calls a function that reads the file and converts its contents into chunks. Those chunks are then stored into ChromaDB - a vector database used to store our information - and will eventually be sent as the context for Groq to use.

## How it Works (So far...)

### 1st: Install Requirements

After cloning the repository, pip install all the necessary requirements. They are found in requirements.txt.

### 2nd: Start the API

Change your directory to the "okada-hackathon" directory. Once there, run the command "uvicorn app.main:app --reload" and wait for the server to start.

### 3rd: Send a POST request

I personally used the Postman extension on Visual Studio Code to test this, but other clients should work all the same. Once the server is live, submit a POST request to "http://localhost:8000/chat" with the following raw JSON as content:

        {
            "message":"{your_prompt_here}"
        }

Because their is context being fed to Groq, you can make your prompt specific to the mock data. However, the limits here are that it only takes a portion of the data it was fed. This is because we need to be considerate of the AI's context limit, which can only accept so much data. Giving it too big of a dataset could cause errors. A message I've sent and seen results with is as follows:

        {
            "message":"What are the unique_id's of the properties you were given? Additionally, was is the average of those properties' size in square feet?"
        }

The response received was as follows:

        {
            "response":"Based on the provided data, the unique IDs of the properties are:\n\n* 66\n* 61\n* 69\n\nThese IDs are likely corresponding to specific properties in the 9 Times Square building.\n\nAs for the average size of the properties in square feet, we can extract the size information from the data:\n\n* Property 66: 15,759 sqft\n* Property 61: 14,188 sqft\n* Property 69: 16,770 sqft\n\nTo calculate the average size, we can add up the sizes and divide by the number of properties:\n\n(15,759 + 14,188 + 16,770) / 3 = 46,717 / 3 = 15,572.33 sqft\n\nSo, the average size of the properties is approximately 15,572.33 square feet."
        }

## Concluding Thoughts

I would like to thank those at Okada & Co. for giving me the opportunity to compete in their Hackathon tournament. I apologize if my project is a bit of a disappointment given what was expected, but I learned quite a bit from the experience. Furthermore, this is a project I want to keep expanding on over the coming weeks. It's a very interesting topic I didn't think I was technically savy enough to venture out towards, but now I have a bit more confidence in my capabilities and am eager to see what else I can do to make this project more applicable in a real-world setting.
