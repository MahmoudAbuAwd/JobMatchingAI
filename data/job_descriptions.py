import pandas as pd
import random

job_data = {
    'job_id': [f'JD{1000+i}' for i in range(20)],
    'title': ['Software Engineer', 'Data Scientist', 'Marketing Manager', 
              'Product Manager', 'HR Specialist', 'Financial Analyst',
              'UX Designer', 'DevOps Engineer', 'Sales Representative',
              'Content Writer', 'Cybersecurity Analyst', 'AI Researcher',
              'Business Analyst', 'Network Administrator', 'Digital Marketer',
              'Operations Manager', 'Graphic Designer', 'Database Administrator',
              'Customer Support', 'Technical Writer'],
    'description': [
        'Develop and maintain software applications using Python and Java. Experience with Django/Flask required.',
        'Analyze complex datasets to extract insights. Proficient in Python, R, SQL, and machine learning frameworks.',
        'Develop marketing strategies and campaigns. Strong communication and analytical skills required.',
        'Lead product development from conception to launch. Experience with Agile methodologies preferred.',
        'Manage recruitment and employee relations. Knowledge of labor laws and HR best practices.',
        'Prepare financial reports and forecasts. Advanced Excel skills and accounting knowledge required.',
        'Design user interfaces and experiences. Proficiency in Figma and Adobe Creative Suite.',
        'Implement and maintain CI/CD pipelines. Experience with AWS, Docker, and Kubernetes.',
        'Generate leads and close sales. Strong interpersonal skills and target-driven mindset.',
        'Create engaging content for websites and social media. Excellent writing and research skills.',
        'Protect systems from cyber threats. Knowledge of ethical hacking and security protocols.',
        'Conduct research in artificial intelligence. PhD preferred with publications in ML conferences.',
        'Analyze business processes and recommend improvements. Strong problem-solving skills required.',
        'Maintain and troubleshoot network infrastructure. CCNA certification preferred.',
        'Develop and execute digital marketing campaigns. Experience with SEO and PPC required.',
        'Oversee daily operations and improve efficiency. Strong leadership and organizational skills.',
        'Create visual content for branding and marketing. Proficiency in Adobe Illustrator and Photoshop.',
        'Manage and optimize database systems. Experience with SQL and NoSQL databases.',
        'Provide excellent customer service and resolve issues. Patience and communication skills essential.',
        'Create technical documentation and manuals. Ability to explain complex concepts simply.'
    ],
    'required_skills': [
        'Python, Java, Django, Flask, OOP',
        'Python, R, SQL, Machine Learning, Statistics',
        'Marketing, Communication, Analytics, Social Media',
        'Product Management, Agile, Market Research, Leadership',
        'HR, Recruitment, Labor Laws, Communication',
        'Finance, Accounting, Excel, Financial Modeling',
        'UI/UX, Figma, Adobe Creative Suite, Prototyping',
        'AWS, Docker, Kubernetes, CI/CD, Linux',
        'Sales, Negotiation, Communication, CRM',
        'Writing, Research, SEO, Content Management',
        'Cybersecurity, Ethical Hacking, Network Security',
        'Machine Learning, Research, Python, TensorFlow',
        'Business Analysis, Problem Solving, Data Visualization',
        'Networking, CCNA, Troubleshooting, Security',
        'Digital Marketing, SEO, PPC, Analytics',
        'Operations, Leadership, Process Improvement',
        'Graphic Design, Adobe Illustrator, Photoshop',
        'SQL, Database Management, Performance Tuning',
        'Customer Service, Problem Solving, Communication',
        'Technical Writing, Documentation, Communication'
    ],
    'experience_level': [
        'Mid-level', 'Senior', 'Mid-level', 'Senior', 'Entry-level',
        'Mid-level', 'Mid-level', 'Senior', 'Entry-level', 'Entry-level',
        'Senior', 'Senior', 'Mid-level', 'Mid-level', 'Mid-level',
        'Senior', 'Mid-level', 'Senior', 'Entry-level', 'Mid-level'
    ]
}

job_df = pd.DataFrame(job_data)
job_df.to_csv('data/job_descriptions.csv', index=False)