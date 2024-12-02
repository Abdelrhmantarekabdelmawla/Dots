## BMC
https://drive.google.com/file/d/1gwJQ9ehk8LZJvAsEJ4nnAu3Wu7SgPP89/view?usp=drive_link
## Video
https://drive.google.com/file/d/16GorG9XY_pTAxGKtffvCATg3BV8Kf1ZE/view?usp=drive_link
## Presentation
https://www.canva.com/design/DAGYIRjRDeA/it2JgLT8TTPb1G6v9FhbbQ/edit?utm_content=DAGYIRjRDeA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
## Prototype
https://www.figma.com/proto/GoBtGdwi42qUE6CNOOQ33V/Dots-Project?node-id=2-866&t=OA0wC5MdWpTmZPGM-1
![Group 3](https://github.com/user-attachments/assets/387b1501-0436-4629-81ee-e9791a3160f1)

## AI-Based Technical Field Recommender

This project utilizes a conversational AI model to guide users through a series of questions and recommend a technical career path or area of expertise.

---

## Model Description

- **Model Type**: Generative conversational AI.
- **Core Functionality**:
  - Asks a sequence of 10 multiple-choice questions.
  - Analyzes user responses to recommend a technical field (e.g., data science, web development).
  - Provides detailed feedback and justification for the recommendation.
- **API Used**: Gemini API for generative content.

---

## Requirements

To run this project, ensure the following:

- Python 3.8 or higher
- Libraries:
  - `numpy`
  - `langchain`
  - `IPython`
  - `google-generativeai`

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Steps to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Dots.git
   cd your-repo-name
   ```

2. **API Configuration**
   - Obtain an API key for Gemini.
   - Update the `api_key` variable in the notebook.

3. **Run the Notebook**
   Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
   Open `DEMO.ipynb` and execute cells sequentially.

4. **Interact with the Model**
   - Start the conversation by running the provided functions.
   - Answer the questions interactively.
   - View the analysis and recommendation at the end.

---
## Example Use Case

The model will ask you 10 questions, such as:

**How much do you enjoy working with computers and technology in your free time?**    
a) Not at all. I prefer other hobbies.    
b) Occasionally, but it's not a major interest.   
c) Frequently; I enjoy learning about and using new technologies.   
d) Very much; I actively seek out new technological challenges and projects.

At the end of the conversation, you will receive a personalized recommendation, e.g.:

**Recommended Field**: Data Science  
**Reasoning**: Aligns with your methodical approach, interest in problem-solving, and comfort with mathematical concepts.

---

Let me know if you'd like to include additional details or further customize this!
