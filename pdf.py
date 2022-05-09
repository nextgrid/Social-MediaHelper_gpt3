import os
import time
# docs: 
# https://pyfpdf.readthedocs.io/en/latest/
# http://www.fpdf.org/en/doc/index.php
# https://pyfpdf.github.io/fpdf2/index.html
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super(PDF, self).__init__()
        # Fonts from fpdf2 
        self.add_font('norasi', fname=os.path.join('fonts/Norasi.ttf'))
        self.set_font('norasi')

    def __call__(self, title, content, question, hashtags):
        self.build_article(title, content, question, hashtags)

    def write_text(self, txt, font_size=14):
        self.set_font_size(size=font_size)

        # fpdf uses latin-1 so we have to encode out txt into it, to prevent errors
        # txt = bytes(txt, 'utf-8').decode('latin-1')
        self.multi_cell(
            200, 10, txt=txt, align='L', new_x="LEFT"
        )

    def build_article(self, title, content, question, hashtags):
        self.add_page()
        
        self.write_text(title, 18)
        self.write_text(question, 12)
        self.write_text(content)
        self.write_text(hashtags, 12)

        if not os.path.isdir('./pdfs'):
            os.mkdir('./pdfs')

        filename = f'art-{time.time()}.pdf'
        self.output(os.path.join('pdfs', filename))

        return filename

if __name__ == '__main__':
    # Test
    s = 'Artificial intelligence is an increasingly hot topic – but what exactly is it? AI is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. AI applications can include things like advanced web search engines, recommendation systems, understanding human speech, self-driving cars, and competing at the highest level in strategic game systems. As machines become more and more capable, the definition of AI continues to evolve. So far, AI has had a huge impact on our world and is only expected to keep growing. What do you think about the role of AI in our lives?'

    t = 'The Benefits and Dangers of AI'
    q = 'What are the most popular applications for artificial intelligence?'
    h = '#ArtificialIntelligence #AI #MachineLearning'
    
    pdf = PDF()
    pdf(t, s, q, h)