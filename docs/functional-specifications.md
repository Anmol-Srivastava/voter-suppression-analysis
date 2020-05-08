





Functional Requirements (sometimes called functional specification):
This should motivate what is being built and describes the use cases. This document should have at minimum two detailed use cases.


The functional specification details:

who are the users and what do they know (e.g., business analyst)
what information users want from the system (e.g., where to put bicycles)
use cases - how users interact with the system to get the information they want
For tool projects, the users are typically programmers, and so the functional specification describes the programming interface.


Project Structure
Projects should have a online github repository with the project name. Top level folders/files within the repository include:

README.md file that gives an overview of the project
LICENSE file
setup.py file that initializes the project after it has been cloned
doc folder that contains documentation (including the functional specification, the design specification, and the final project presentation or poster)
python package folder (with the same name as the repository) that is structured as one or more python modules (e.g., with init.py files) and test files that begin with “test_”.
examples folder that contains examples of using the packages




Design Documents
You will create two documents describing the design of your project. These documents should be in your project docs folder.

Functional Specification. The document should have the following sections:
Background. The problem being addressed.
User profile. Who uses the system. What they know about the domain and computing (e.g., can browse the web, can program in Python)
Data sources. What data you will use and how it is structured.
Use cases. Describing at least two use cases. For each, describe: (a) the objective of the user interaction (e.g., withdraw money from an ATM); and (b) the expected interactions between the user and your system.
Component Specification. The document should have sections for.
Software components. High level description of the software components such as: data manager, which provides a simplified interface to your data and provides application specific features (e.g., querying data subsets); and visualization manager, which displays data frames as a plot. Describe at least 3 components specifying: what it does, inputs it requires, and outputs it provides.
Interactions to accomplish use cases. Describe how the above software components interact to accomplish at least one of your use cases.
Preliminary plan. A list of tasks in priority order



Technology Review Presentation
The technology review is about making decisions about the choice of a python library to address a technology need in the project. For example, many projects make use of map visualizations. There are many python libraries that support these visualizations such as Bokeh, Dash, and googlemaps. The libraries have different capbilities, such as what (if any) interactions users can have with the map. You will want to choose a library that: (a) addresses the requirements of your project; (b) is compatible with other elements of your project (e.g., runs on python 3); (c) is relatively easy to use; (d) is computationally efficient for the scale of data you use; and (d) doesn’t have software bugs that will impair your use cases.

The technology review is a group presentation. It should be about 5-7 minutes in length. The presentation should address the following:

Brief background on the problem you’re solving to motivate a technology for which you need a python library (e.g., interactive maps).
One slide desciption of a use case in which the technology is required.
One slide that describes at least two python libraries that potentially address your technology requirement.
One slide side-by-side comparisons of the technologies. This will require that you actually install and use the technologies.