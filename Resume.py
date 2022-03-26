from dataclasses import dataclass

import matplotlib.pyplot as plt


@dataclass
class PersonalInfo:
    header = None
    name = None
    title = None
    contact = None


# Text Variables
Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my portfolio.'
Name = 'EDDIE KIRKLAND'
Title = 'Data Science & Analytics'
Contact = 'Atlanta, GA\n404-XXX-XXXX\nwekrklndATgmailDOTcom\nlinkedin.com/in/ekirkland\ngithub.com/e-kirkland'


@dataclass
class Projects:
    header = "PROJECTS/PUBLICATIONS"
    title_list = list()
    description_list = list()
    website = None


ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Increasing Kaggle Revenue'
ProjectOneDesc = '- Published by Towards Data Science\n- Analyzed user survey to recommend most profitable future ' \
                 'revenue source\n- Cleaned/visualized data using pandas/matplotlib libraries in Python '
ProjectTwoTitle = 'NYC School Data Cleaning & Analysis'
ProjectTwoDesc = '- Cleaned and combined several tables using pandas library in Python\n- Used PDE and visualization ' \
                 'to determine correlations for future study '
ProjectThreeTitle = 'Pandas Cleaning and Visualization'
ProjectThreeDesc = '- Cleaned data for analysis using pandas library in Python\n- Used pandas and matplotlib to ' \
                   'explore which cars hold the most value over time '
Portfolio = 'Portfolio: rebrand.ly/ekirkland'


@dataclass
class Experience:
    header = "EXPERIENCE"
    title_list = list()
    time_list = list()
    description_list = list()


WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Example Company / Example Position'
WorkOneTime = '8/2013-Present'
WorkOneDesc = '- Raised $350k in startup funds, recruited/organized launch team\n- Coordinated branding and ' \
              'communication strategy\n- Led team of 80 volunteer and staff leaders '
WorkTwoTitle = 'Second Company / Second Position'
WorkTwoTime = '2/2007-8/2013'
WorkTwoDesc = '- Led team of over 100 full-time and contract staff\n- Helped create branding and messaging for' \
              ' weekly content\n- Created/directed musical elements at weekly events for up to 10,000 people '
WorkThreeTitle = 'Third Company / Third Position'
WorkThreeTime = '6/2004-2/2007'
WorkThreeDesc = '- Planned/Coordianted Toronto arena event and South Africa speaking tour\n- Oversaw research for ' \
                'published products '


@dataclass
class Education:
    header = "EDUCATION"
    title_list = list()
    time_list = list()
    description_list = list()


EduHeader = 'EDUCATION'
EduOneTitle = 'Example University, Bachelor of Business Administration'
EduOneTime = '2000-2004'
EduOneDesc = '- Major: Management, Minor: Statistics'
EduTwoTitle = 'Example University, Master of Arts'
EduTwoTime = '2013-2017'


@dataclass
class Skills:
    header = "Skills"
    description_list = list()


SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Pandas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Command Line\n- Git and Version ' \
             'Control\n- SQL\n- APIs\n- Probability/Statistics\n- Data Manipulation\n- Excel '


@dataclass
class Extras:
    titles = list()
    description = list()


ExtrasTitle = 'DataQuest\nData Scientist Path'
ExtrasDesc = 'Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand ' \
             'statistical analysis '
CodeTitle = 'View Portfolio'  # Setting style for bar graphs


# %matplotlib inline# set font
class Design:
    def setup_graph(self):
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))  # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
        plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)  # set background color
        ax.set_facecolor('white')  # remove axes
        plt.axis('off')  # add text

    def _build_personal(self, personal: PersonalInfo):
        plt.annotate(personal.header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(personal.name, (.02, .94), weight='bold', fontsize=20)
        plt.annotate(personal.title, (.02, .91), weight='regular', fontsize=14)
        plt.annotate(personal.contact, (.7, .906), weight='regular', fontsize=8, color='#ffffff')

    def _build_projects(self, projects: Projects):
        plt.annotate(projects.header, (.02, .86), weight='bold', fontsize=10, color='#58C1B2')
        # get in loop
        plt.annotate(ProjectOneTitle, (.02, .832), weight='bold', fontsize=10)
        plt.annotate(ProjectOneDesc, (.04, .78), weight='regular', fontsize=9)
        plt.annotate(ProjectTwoTitle, (.02, .745), weight='bold', fontsize=10)
        plt.annotate(ProjectTwoDesc, (.04, .71), weight='regular', fontsize=9)
        plt.annotate(ProjectThreeTitle, (.02, .672), weight='bold', fontsize=10)
        plt.annotate(ProjectThreeDesc, (.04, .638), weight='regular', fontsize=9)
        # website = portfolio
        plt.annotate(projects.website, (.02, .6), weight='bold', fontsize=10)

    def _build_experience(self, experience: Experience):
        plt.annotate(experience.header, (.02, .54), weight='bold', fontsize=10, color='#58C1B2')
        # get in loop
        plt.annotate(WorkOneTitle, (.02, .508), weight='bold', fontsize=10)
        plt.annotate(WorkOneTime, (.02, .493), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(WorkOneDesc, (.04, .445), weight='regular', fontsize=9)
        plt.annotate(WorkTwoTitle, (.02, .4), weight='bold', fontsize=10)
        plt.annotate(WorkTwoTime, (.02, .385), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(WorkTwoDesc, (.04, .337), weight='regular', fontsize=9)
        plt.annotate(WorkThreeTitle, (.02, .295), weight='bold', fontsize=10)
        plt.annotate(WorkThreeTime, (.02, .28), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(WorkThreeDesc, (.04, .247), weight='regular', fontsize=9)

    def _build_education(self, education: Education):
        plt.annotate(education.header, (.02, .185), weight='bold', fontsize=10, color='#58C1B2')
        # get in loop
        plt.annotate(EduOneTitle, (.02, .155), weight='bold', fontsize=10)
        plt.annotate(EduOneTime, (.02, .14), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(EduOneDesc, (.04, .125), weight='regular', fontsize=9)
        plt.annotate(EduTwoTitle, (.02, .08), weight='bold', fontsize=10)
        plt.annotate(EduTwoTime, (.02, .065), weight='regular', fontsize=9, alpha=.6)

    def _build_skill(self, skills: Skills):
        plt.annotate(skills.header, (.7, .8), weight='bold', fontsize=10, color='#ffffff')
        # get in loop
        plt.annotate(SkillsDesc, (.7, .56), weight='regular', fontsize=10, color='#ffffff')

    def _build_extras(self, extras: Extras):
        plt.annotate(ExtrasTitle, (.7, .43), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(ExtrasDesc, (.7, .345), weight='regular', fontsize=10, color='#ffffff')
        plt.annotate(CodeTitle, (.7, .2), weight='bold', fontsize=10, color='#ffffff')  # add qr code

    def _build_file(self, file_base_name: str):
        # get in loop
        plt.savefig(f'{file_base_name}.pdf', dpi=300, bbox_inches='tight')
        # get in loop
        plt.savefig(f'{file_base_name}.png', dpi=300, bbox_inches='tight')

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# arr_code = mpimg.imread('ekresumecode.png')
# imagebox = OffsetImage(arr_code, zoom=0.5)
# ab = AnnotationBbox(imagebox, (0.84, 0.12))
# ax.add_artist(ab)

