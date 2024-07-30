"""
The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class but lets subclasses override specific steps of the algorithm
without changing its structure. This pattern is useful for creating a framework where some steps are fixed, while others can be customized by subclasses.

*** Purpose ***
The primary purpose of the Template Method Pattern is to provide a common algorithm structure while allowing specific steps to be customized by subclasses. This ensures consistency in the overall process while providing flexibility in the details of individual steps.

*** Intuition ***
Imagine you are developing a financial report generation system. The process of generating a report might involve several steps, such as gathering data, calculating metrics, and formatting the output. While the overall process is consistent, the specifics of data gathering and formatting may vary depending on the type of report. The Template Method Pattern allows you to define a general structure for report generation while letting subclasses customize specific parts.

*** Structure ***
1. Abstract Class: Defines the template method and the steps of the algorithm. Some steps are abstract and must be implemented by concrete subclasses.
2. Concrete Subclasses: Implement the specific steps of the algorithm defined by the abstract class.

*** Example: Financial Report Generation ***
Let's consider an example where we generate different types of financial reports, such as profit and loss reports and balance sheets.

"""

#======================================== Abstract Class ========================================

# Define the abstract class with the template method and abstract steps

from abc import ABC, abstractmethod

class FinancialReport(ABC):
    def generate_report(self):
        self.gather_data()
        self.calculate_metrics()
        self.format_report()
        self.print_report()

    @abstractmethod
    def gather_data(self):
        pass

    @abstractmethod
    def calculate_metrics(self):
        pass

    @abstractmethod
    def format_report(self):
        pass

    def print_report(self):
        print("Printing the report...")

#======================================== Concrete Subclasses ========================================

# Implement the concrete subclasses for different types of reports

class ProfitLossReport(FinancialReport):
    def gather_data(self):
        print("Gathering data for profit and loss report.")

    def calculate_metrics(self):
        print("Calculating metrics for profit and loss report.")

    def format_report(self):
        print("Formatting profit and loss report.")

class BalanceSheetReport(FinancialReport):
    def gather_data(self):
        print("Gathering data for balance sheet report.")

    def calculate_metrics(self):
        print("Calculating metrics for balance sheet report.")

    def format_report(self):
        print("Formatting balance sheet report.")


#======================================== Client Code ========================================

# Use the template method pattern to generate reports

if __name__ == "__main__":
    # Generate a profit and loss report
    pl_report = ProfitLossReport()
    pl_report.generate_report()
    # Output:
    # Gathering data for profit and loss report.
    # Calculating metrics for profit and loss report.
    # Formatting profit and loss report.
    # Printing the report...

    # Generate a balance sheet report
    bs_report = BalanceSheetReport()
    bs_report.generate_report()
    # Output:
    # Gathering data for balance sheet report.
    # Calculating metrics for balance sheet report.
    # Formatting balance sheet report.
    # Printing the report...

#======================================== How It Works ========================================

"""
1. Abstract Class

 - FinancialReport defines the generate_report template method, which outlines the steps of the report generation process. It also provides the print_report method as a default implementation.
 - The gather_data, calculate_metrics, and format_report methods are abstract and must be implemented by subclasses.

2. Concrete Subclasses
ProfitLossReport and BalanceSheetReport implement the abstract methods, providing specific details for gathering data, calculating metrics, and formatting the report.

3. Client Code
The client creates instances of the concrete subclasses and calls the generate_report method. The template method ensures that the overall process remains consistent while allowing customization of specific steps.

"""
