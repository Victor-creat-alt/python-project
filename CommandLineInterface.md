# Health Simplified CLI Application

This document explains how to run and use the Health Simplified CLI for managing users, food entries, goals, reports, and meal plans.

---

## 1. **Install Requirements**

Make sure you have Python 3.8+ and PostgreSQL installed.  
Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 2. **Set Up the Database**

Ensure PostgreSQL is running and create the database if needed:

```bash
psql -U victor
CREATE DATABASE health;
```

---

## 3. **Run the CLI**

From your project directory, run:

```bash
python main.py --help
```

This will show all available commands.

---

## 4. **Available Commands and Usage**

### **User Commands**
- Create a user:
  ```bash
  python main.py user-create --name "Alice"
  ```
- List all users:
  ```bash
  python main.py user-list
  ```

### **Food Entry Commands**
- Create a food entry:
  ```bash
  python main.py food-entry-create --user-id 1 --food-name "Apple" --calories 95 --meal-type "breakfast" --quantity 1 --date "2025-05-28 08:00:00"
  ```
- List food entries:
  ```bash
  python main.py food-entry-list --user-id 1
  ```
- Update a food entry:
  ```bash
  python main.py entry-update --id 1 --calories 100
  ```
- Delete a food entry:
  ```bash
  python main.py entry-delete --id 1
  ```

### **Goal Commands**
- Create a goal:
  ```bash
  python main.py goal-create --user-id 1 --daily-calories 2000 --weekly-calories 14000
  ```
- List goals:
  ```bash
  python main.py goal-list --user-id 1
  ```
- Update a goal:
  ```bash
  python main.py update-goal --id 1 --daily-calories 2100 --weekly-calories 14700
  ```
- Delete a goal:
  ```bash
  python main.py goal-delete --id 1
  ```

### **Report Commands**
- Generate a report:
  ```bash
  python main.py report-generate --user-id 1 --date "2025-05-28 00:00:00"
  ```
- List reports:
  ```bash
  python main.py report-list --user-id 1
  ```
- Update a report:
  ```bash
  python main.py update-report --id 1 --total-calories 1800
  ```
- Delete a report:
  ```bash
  python main.py delete-report --id 1
  ```

### **Meal Plan Commands**
- Create a meal plan:
  ```bash
  python main.py meal-plan-create --user-id 1 --week-number 22 --planned-meals "Chicken, Rice" --nutrition-balance "High Protein"
  ```
- List meal plans:
  ```bash
  python main.py meal-plan-list --user-id 1
  ```
- Update a meal plan:
  ```bash
  python main.py update-meal-plan --id 1 --planned-meals "Fish, Salad"
  ```
- Delete a meal plan:
  ```bash
  python main.py delete-meal-plan --id 1
  ```

---

## 5. **Get Help for Any Command**

For detailed usage of any command, use:

```bash
python main.py <command> --help
```

Example:

```bash
python main.py food-entry-create --help
```

---

## 6. **Notes**

- All changes are saved to the PostgreSQL database specified in `main.py`.
- Make sure your database server is running before using the CLI.
- If you encounter errors, check your database connection and model definitions.

---
```<!-- filepath: /home/victor/python-project/CommandLineInterface.md -->

# Health Simplified CLI Application

This document explains how to run and use the Health Simplified CLI for managing users, food entries, goals, reports, and meal plans.

---

## 1. **Install Requirements**

Make sure you have Python 3.8+ and PostgreSQL installed.  
Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 2. **Set Up the Database**

Ensure PostgreSQL is running and create the database if needed:

```bash
psql -U victor
CREATE DATABASE health_tracker;
```

---

## 3. **Run the CLI**

From your project directory, run:

```bash
python main.py --help
```

This will show all available commands.

---

## 4. **Available Commands and Usage**

### **User Commands**
- Create a user:
  ```bash
  python main.py user-create --name "Alice"
  ```
- List all users:
  ```bash
  python main.py user-list
  ```

### **Food Entry Commands**
- Create a food entry:
  ```bash
  python main.py food-entry-create --user-id 1 --food-name "Apple" --calories 95 --meal-type "breakfast" --quantity 1 --date "2025-05-28 08:00:00"
  ```
- List food entries:
  ```bash
  python main.py food-entry-list --user-id 1
  ```
- Update a food entry:
  ```bash
  python main.py entry-update --id 1 --calories 100
  ```
- Delete a food entry:
  ```bash
  python main.py entry-delete --id 1
  ```

### **Goal Commands**
- Create a goal:
  ```bash
  python main.py goal-create --user-id 1 --daily-calories 2000 --weekly-calories 14000
  ```
- List goals:
  ```bash
  python main.py goal-list --user-id 1
  ```
- Update a goal:
  ```bash
  python main.py update-goal --id 1 --daily-calories 2100 --weekly-calories 14700
  ```
- Delete a goal:
  ```bash
  python main.py goal-delete --id 1
  ```

### **Report Commands**
- Generate a report:
  ```bash
  python main.py report-generate --user-id 1 --date "2025-05-28 00:00:00"
  ```
- List reports:
  ```bash
  python main.py report-list --user-id 1
  ```
- Update a report:
  ```bash
  python main.py update-report --id 1 --total-calories 1800
  ```
- Delete a report:
  ```bash
  python main.py delete-report --id 1
  ```

### **Meal Plan Commands**
- Create a meal plan:
  ```bash
  python main.py meal-plan-create --user-id 1 --week-number 22 --planned-meals "Chicken, Rice" --nutrition-balance "High Protein"
  ```
- List meal plans:
  ```bash
  python main.py meal-plan-list --user-id 1
  ```
- Update a meal plan:
  ```bash
  python main.py update-meal-plan --id 1 --planned-meals "Fish, Salad"
  ```
- Delete a meal plan:
  ```bash
  python main.py delete-meal-plan --id 1
  ```

---

## 5. **Get Help for Any Command**

For detailed usage of any command, use:

```bash
python main.py <command> --help
```

Example:

```bash
python main.py food-entry-create --help
```

---

## 6. **Notes**

- All changes are saved to the PostgreSQL database specified in `main.py`.
- Make sure your database server is running before using the CLI.
- If you encounter errors, check your database connection and model definitions.

---