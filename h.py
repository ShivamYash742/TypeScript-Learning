# Re-generate the cleaned resume PDF since the session expired

from fpdf import FPDF
import re

# Resume text without emojis
resume_text = """
SHIVAM MISHRA
B.Tech Student in Computer Science Engineering

New Delhi, India | +91-9871576382 | shivamyash742@gmail.com  
Portfolio: https://personal-portfolio-shivam-site.vercel.app/  
LinkedIn: https://www.linkedin.com/in/ShivamYash742  
GitHub: https://github.com/ShivamYash742

---

SUMMARY
I’m a passionate B.Tech CSE student and aspiring full-stack developer with a strong foundation in React, Node.js, and AI-driven applications. I’ve led multiple hackathon teams, contributed to real-world web apps, and currently serve as a web committee member at IEEE MSIT. Experienced in building scalable, user-centric projects with modern tools and practices.

---

EDUCATION
Bachelor of Technology - Computer Science Engineering  
Guru Gobind Singh Indraprastha University, New Delhi  
09/2023 – 06/2027  
SGPA: 8.72 / 10

---

EXPERIENCE
Website Developer – E-Cell Team  
10/2024 – Present  
- Developed and optimized the official E-Cell website with responsive UI and seamless navigation.  
- Implemented full-stack features including RESTful API integrations to enhance user engagement.

Team Leader – Code Breakers, HackWithMAIT 5.0  
10/2024 – Present  
- Led a 4-member team, prototyped an Android crypto mining app in 24 hours.  
- Ranked in the top 30% of submissions, showcasing innovation under pressure.

Event Head – Code Combat: DSA Marathon, Avensis 2025  
01/2025  
- Designed DSA problems, coordinated logistics, and handled 100+ participants’ queries.

Team Coordinator – Hackwie, IEEE MSIT  
01/2025  
- Helped organize and streamline team selections during the IEEE hackathon.

---

PROJECTS
Image Format Converter  
GitHub Repo: https://github.com/ShivamYash742/Image-format-convertor  
React, Express.js, Node.js, TailwindCSS  
- Full-stack web tool to convert, resize, and compress images across JPG, PNG, WebP.  
- Enabled auto-format detection and added dynamic resizing for flexibility.

AI Feedback Analyzer (In Progress)  
GitHub Repo: https://github.com/ShivamYash742/AIFEEDBACK  
Next.js, MongoDB, Express.js, Gemini API, NLP  
- NLP-based app that analyzes customer reviews and generates seller insights.  
- Integrates AI APIs to extract sentiment and recommend improvements.

To-Do App (React)  
GitHub Repo: https://github.com/ShivamYash742/To-Do-App-React  
- Task management app using React hooks and reusable components.

Weather App  
GitHub Repo: https://github.com/ShivamYash742/WeatherAPP-react  
- Real-time weather updates via external APIs with user-friendly UI.  
- Achieved compatibility across 100% of tested devices.

---

SKILLS
Languages: C++, C, Python (Tkinter), JavaScript, HTML5, CSS3  
Frontend: React.js, Next.js, TailwindCSS  
Backend: Node.js, Express.js  
Database: MongoDB, Firebase  
Tools & Platforms: Git, GitHub, Vercel, Netlify  
Other: REST APIs, NLP, AI APIs, Responsive Design

---

TRAINING / COURSEWORK
- Web Development  
- Data Structures & Algorithms  
- Artificial Intelligence

---

STRENGTHS & ACHIEVEMENTS
- Leadership Excellence: Guided multiple teams through technical challenges under deadlines.  
- Hackathon Innovator: Ranked in the top 30% of HackWithMAIT 5.0 for innovative prototyping.  
- Academic Consistency: Maintained a strong SGPA of 8.72/10 alongside active project contributions.
"""

# Clean any remaining non-ASCII characters
clean_resume_text = re.sub(r'[^\x00-\x7F]+', '', resume_text)

# Create the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=11)

for line in clean_resume_text.strip().split('\n'):
    if line.strip() == "---":
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.3)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(2)
    else:
        pdf.multi_cell(0, 10, line.strip())


pdf.output(" resume.pdf")
