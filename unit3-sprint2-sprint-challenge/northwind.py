"""
Run queries on Northwind data for Sprint challenge
"""
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')

def n_run_query(query):
    curs = conn.cursor()
    print(curs.execute(query).fetchall())
    conn.commit()
    curs.close()

def n_do_tasks():
    #part 2 of sprint Challenge
    # What are the ten most expensive items (per unit price) in the database?
    print('\nThe ten most expensive items (per unit price):\n')
    n_run_query("""
    SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;
    """)
    # What is the average age of an employee at the time of their hiring? (Hint: a
    # lot of arithmetic works with dates.)
    print('\nThe average age of an employee at time of hire:\n')
    n_run_query("""
    SELECT AVG(HireDate - BirthDate) FROM Employee;
    """)

    # (*Stretch*) How does the average age of employee at hire vary by city?
    print('\nThe Average Age by City:\n')
    avg_age_city = """
    SELECT AVG(HireDate - BirthDate), City FROM Employee GROUP BY City;
    """
    n_run_query(avg_age_city)


    #part 3 of sprint Challenge
    # What are the ten most expensive items (per unit price) in the database
    #*and* their suppliers?
    print('\n\nThe ten most expensive items (per unit) and their suppliers:\n')
    sup_items = """
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Supplier
    INNER JOIN Product ON Supplier.ID=Product.SupplierID
    ORDER BY Product.UnitPrice DESC LIMIT 10;
    """
    n_run_query(sup_items)
    #What is the largest category (by number of unique products in it)?
    cat_prod = """
    SELECT Category.CategoryName, MAX(DISTINCT Product.ProductName) AS PN
    FROM Category
    INNER JOIN Product ON Product.SupplierID=Category.ID
    """
    print('\nThe Largest Category (by number of unique products):\n')
    n_run_query(cat_prod)
    #(*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
    emp_terr = """
    SELECT Employee.FirstName, Employee.LastName,
    MAX(DISTINCT EmployeeTerritory.TerritoryID)
    FROM Employee
    INNER JOIN EmployeeTerritory ON
    EmployeeTerritory.EmployeeId=Employee.Id
    """
    print('\nEmployee with the most territories\n')
    n_run_query(emp_terr)

if __name__ == "__main__":
    n_do_tasks()
