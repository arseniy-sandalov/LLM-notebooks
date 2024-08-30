test_dataset = [
    {
        "question": "Which employees are certified in project management?",
        "relevant_tables": "employees, certification"
    },
    {
        "question": "Who are the employees that worked on project with id 34?",
        "relevant_tables": "employees, mysProjects"
    },
    {
        "question": "Which employees have taken annual leave?",
        "relevant_tables": "employees, leaves"
    },
    {
        "question": "Who are the employees that have received performance evaluations?",
        "relevant_tables": "employees, scores"
    },
    {
        "question": "What are the languages that Ahmed Kasap speak?",
        "relevant_tables": "employees, languages"
    },
    {
        "question": "What was the high school of Zeynep Yilmaz?",
        "relevant_tables": "employees, educations"
    },
    {
        "question": "What are comments that Mehmet Osman wrote about Suleyman Basturk?",
        "relevant_tables": "employees, comments"
    },
    {
        "question": "Show the employees who know AutoCAD software",
        "relevant_tables": "employees, softwares"
    },
    {
        "question": "What is the hierarchy level of Ahmed Kasap in the company?",
        "relevant_tables": "employees, orgHierarchy"
    },
    {
        "question": "What was the previous working place of Ahmed Kasap?",
        "relevant_tables": "employees, workHistory"
    }, 
    {
        "question": "Which employees have experience with 'Artificial Intelligence' and have 'Python' skills?",
        "relevant_tables": "employees, softwares, mysProjects"
    },
    {
        "question": "List employees who are currently working on 'Marketing' projects and have 'Content Creation' skills.",
        "relevant_tables": "employees, mysProjects, softwares"
    },
    {
        "question": "Retrieve the languages spoken by employees who have 'Data Engineering' experience.",
        "relevant_tables": "employees, languages"
    },
    {
        "question": "Show the certifications for employees who have 'Project Management' and 'Agile' training.",
        "relevant_tables": "employees, certification"
    },
    {
        "question": "Find employees who have completed 'Data Science' training and have 'R' programming skills.",
        "relevant_tables": "employees, certification, softwares"
    },
    {
        "question": "List employees who are fluent in 'German' and have 'Business Intelligence' experience.",
        "relevant_tables": "employees, languages, softwares"
    },
    {
        "question": "Retrieve the educational background for employees who have a degree in 'Physics' from 'MIT'.",
        "relevant_tables": "employees, educations"
    },
    {
        "question": "Show the work history for employees who have worked on 'Web Development' projects and have 'HTML' skills.",
        "relevant_tables": "employees, workHistory, softwares"
    },
    {
        "question": "List employees who have 'Project Management' certifications and have worked on 'Infrastructure' projects.",
        "relevant_tables": "employees, certification, mysProjects"
    },
    {
        "question": "Find employees who are fluent in 'Portuguese' and have 'Machine Learning' certifications.",
        "relevant_tables": "employees, languages, certification"
    },
    {
        "question": "Retrieve the certifications for employees who have 'Cybersecurity' expertise and have completed 'Network Security' courses.",
        "relevant_tables": "employees, certification"
    },
    {
        "question": "Show the project details for employees who have 'Data Science' skills and have worked on 'Predictive Analytics' projects.",
        "relevant_tables": "employees, mysProjects, softwares"
    },
    {
        "question": "List employees who have experience with 'Big Data' and have received 'Hadoop' certification.",
        "relevant_tables": "employees, softwares, certification"
    },
    {
        "question": "Find employees who are fluent in 'Japanese' and have 'Cloud Computing' skills.",
        "relevant_tables": "employees, languages, softwares"
    },
    {
        "question": "Retrieve the work history of employees who have worked on 'E-commerce' and have 'JavaScript' skills.",
        "relevant_tables": "employees, workHistory, softwares"
    },
    {
        "question": "Show the educational qualifications of employees who have a degree in 'Engineering' from 'University of California'.",
        "relevant_tables": "employees, educations"
    },
    {
        "question": "List employees who are fluent in 'Spanish' and have 'Marketing' experience.",
        "relevant_tables": "employees, languages, certification"
    },
    {
        "question": "Find employees who have 'Database Administration' skills and have completed 'SQL' certification.",
        "relevant_tables": "employees, softwares, certification"
    },
    {
        "question": "Retrieve the work history for employees who have experience in 'Healthcare' and have 'Healthcare IT' skills.",
        "relevant_tables": "employees, workHistory, softwares"
    },
    {
        "question": "Show the certifications for employees who have 'Data Visualization' experience and have completed 'Tableau' training.",
        "relevant_tables": "employees, certification"
    },
    {
        "question": "List employees who have 'Artificial Intelligence' skills and have worked on 'Machine Learning' projects.",
        "relevant_tables": "employees, softwares, mysProjects"
    },
    {
        "question": "Find employees who are fluent in 'Korean' and have 'Data Science' certifications.",
        "relevant_tables": "employees, languages, certification"
    }
]
def llm_test(chain, schema):
    question_num = 1 
    counter = 0
    for data_point in test_dataset:
        
        response = chain.invoke({"schema": schema, "prompt": data_point["question"]})
        
        # Extracting the response text from the model
        response_tables = response.get("text", "")  # Extracting the "text" attribute from the response dictionary

        # Convert the tables from the model's response and the correct answer to sets
        model_tables_set = set(response_tables.split(", "))
        correct_tables_set = set(data_point["relevant_tables"].split(", "))
    
        
        if model_tables_set == correct_tables_set:
            print(str(question_num) + ". " + data_point["question"] + " ✅" + "\n" + "Model answer: " + response_tables + "\n" + "Correct answer: " + data_point["relevant_tables"])
            counter += 1
        else:
            print(str(question_num) + ". " + data_point["question"] + " ❌" + "\n" + "Model answer: " + response_tables + "\n" + "Correct answer: " + data_point["relevant_tables"])
        question_num += 1
    print("\n🔴 Model score: " + str(counter) + "/" + str(len(test_dataset)) + " answers.")



