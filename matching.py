# matching.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

class JobResumeMatcher:
    def __init__(self):
        # Load the SentenceTransformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def create_embeddings(self, texts):
        """Create embeddings for a list of texts"""
        return self.model.encode(texts, convert_to_tensor=False)
    
    def calculate_similarity(self, job_embedding, resume_embeddings):
        """Calculate cosine similarity between job embedding and resume embeddings"""
        return cosine_similarity([job_embedding], resume_embeddings)[0]
    
    def match_resumes_to_job(self, job_text, resume_texts, top_n=5):
        """
        Match resumes to a job description
        
        Args:
            job_text (str): Job description text
            resume_texts (list): List of resume texts
            top_n (int): Number of top matches to return
            
        Returns:
            tuple: (similarity_scores, top_indices)
        """
        # Create embeddings
        job_embedding = self.create_embeddings([job_text])[0]
        resume_embeddings = self.create_embeddings(resume_texts)
        
        # Calculate similarities
        similarity_scores = self.calculate_similarity(job_embedding, resume_embeddings)
        
        # Get top N matches
        top_indices = np.argsort(similarity_scores)[-top_n:][::-1]
        
        return similarity_scores, top_indices
    
    def prepare_job_text(self, job_row):
        """Combine relevant job fields into a single text for embedding"""
        return f"{job_row['title']}. {job_row['description']}. Required skills: {job_row['required_skills']}. Experience level: {job_row['experience_level']}"
    
    def prepare_resume_text(self, resume_row):
        """Combine relevant resume fields into a single text for embedding"""
        return f"Skills: {resume_row['skills']}. Education: {resume_row['education']}. Experience: {resume_row['experience_years']} years"
    
    def match_jobs_to_resume(self, resume_text, job_texts, top_n=5):
        """
        Match jobs to a resume
        
        Args:
            resume_text (str): Resume text
            job_texts (list): List of job description texts
            top_n (int): Number of top matches to return
            
        Returns:
            tuple: (similarity_scores, top_indices)
        """
        # Create embeddings
        resume_embedding = self.create_embeddings([resume_text])[0]
        job_embeddings = self.create_embeddings(job_texts)
        
        # Calculate similarities
        similarity_scores = self.calculate_similarity(resume_embedding, job_embeddings)
        
        # Get top N matches
        top_indices = np.argsort(similarity_scores)[-top_n:][::-1]
        
        return similarity_scores, top_indices
    
    def get_matched_results(self, jobs_df, resumes_df, job_id=None, resume_id=None, top_n=5):
        """
        Get matched results either for a specific job or resume
        
        Args:
            jobs_df (pd.DataFrame): DataFrame of job descriptions
            resumes_df (pd.DataFrame): DataFrame of resumes
            job_id (str): ID of job to match resumes to
            resume_id (str): ID of resume to match jobs to
            top_n (int): Number of top matches to return
            
        Returns:
            dict: Dictionary containing matching results
        """
        if job_id:
            # Find matching resumes for a job
            job_row = jobs_df[jobs_df['job_id'] == job_id].iloc[0]
            job_text = self.prepare_job_text(job_row)
            
            resume_texts = [self.prepare_resume_text(row) for _, row in resumes_df.iterrows()]
            
            similarity_scores, top_indices = self.match_resumes_to_job(
                job_text, resume_texts, top_n=top_n
            )
            
            matched_resumes = resumes_df.iloc[top_indices].copy()
            matched_resumes['match_score'] = similarity_scores[top_indices]
            
            return {
                'type': 'job_to_resumes',
                'job': job_row,
                'matches': matched_resumes.to_dict('records'),
                'scores': similarity_scores
            }
            
        elif resume_id:
            # Find matching jobs for a resume
            resume_row = resumes_df[resumes_df['resume_id'] == resume_id].iloc[0]
            resume_text = self.prepare_resume_text(resume_row)
            
            job_texts = [self.prepare_job_text(row) for _, row in jobs_df.iterrows()]
            
            similarity_scores, top_indices = self.match_jobs_to_resume(
                resume_text, job_texts, top_n=top_n
            )
            
            matched_jobs = jobs_df.iloc[top_indices].copy()
            matched_jobs['match_score'] = similarity_scores[top_indices]
            
            return {
                'type': 'resume_to_jobs',
                'resume': resume_row,
                'matches': matched_jobs.to_dict('records'),
                'scores': similarity_scores
            }
        
        else:
            raise ValueError("Either job_id or resume_id must be provided")