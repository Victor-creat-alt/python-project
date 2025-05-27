------------------------------------------------------------------------------------------
USER MODEL
------------------------------------------------------------------------------------------
User -> Food Entry
(One to Many Relationship)
- A Single user can make multiple Food Entries
- Each Food Entry belongs to a particular User(tracking food name, calories, count, date)

User -> Goal
(One to Many Relationship)
- A user can set Multiple Goals
- Each Goal belongs to a particular User(Personal Nutrition Tracking)

User -> Report
(One to Many Relationship)
- A User can Set Multiple Reports(Summarizing food intake)
- Each Report shows calorie totals and nutrition goals

User -> MealPlan
(One to Many Relationship)
- A User can create a MealPlan entries for weekly scheduling
- Each Meal Plan is associated to a User(Organizing planned meals for a specific week)

RELATIONSHIP INTEGRITY
- Cascade Delete => If a user is deleted all associated FoodEntry, Goal, Report and MealPlan records should be removed to achieve organization

------------------------------------------------------------------------------------------
GOAL MODEL (Defines calorie targets per user)
------------------------------------------------------------------------------------------
Attributes
- id (Primary Key, Unique Identifier)
- user_id (Foreign Key → User.id)
- daily_calories (Integer, required, defines target calorie intake per day)
- weekly_calories (Integer, required, defines target calorie intake per week)
- created_at (Timestamp, when the goal was set)
- updated_at (Timestamp, tracks last modification)
Relationships
- Many-to-One: A Goal belongs to a single User but a User can have multiple goals.
- Integrity Rules:
- A User must exist before a Goal can be set.
- If a User is deleted, associated Goals are removed (Cascade Delete).
- A User should only have one active goal at a time.

------------------------------------------------------------------------------------------
FOOD ENTRY MODEL (Logs meals for tracking)
-----------------------------------------------------------------------------------------
Attributes
- id (Primary Key, Unique Identifier)
- user_id (Foreign Key → User.id)
- food_name (String, required, name of the food item)
- calories (Integer, required, amount of calories consumed)
- date (Date, required, food entry timestamp)
- meal_type (String, defines whether meal was Breakfast, Lunch, or Dinner)
- quantity (Integer, optional, number of servings)
- created_at (Timestamp, when entry was logged)

Relationships
- Many-to-One: Each FoodEntry belongs to a User.
- Integrity Rules:
- A User must exist before logging food entries.
- If a User is deleted, all FoodEntry records are also removed (Cascade Delete).

------------------------------------------------------------------------------------------
REPORT MODEL (Summarizes food intake vs. goals)
-----------------------------------------------------------------------------------------
Attributes
- id (Primary Key, Unique Identifier)
- user_id (Foreign Key → User.id)
- date (Date, required, report timestamp)
- total_calories (Integer, computed as sum of calories from food entries)
- goal_status (Boolean, indicates whether user met calorie goal for the day)
- weekly_progress (Float, calculated as percentage of goal met for the week)
- created_at (Timestamp, when report was generated)
Relationships
- Many-to-One: Each Report belongs to a User.
- One-to-One per Day: Only one report per user per day.
- Integrity Rules:
- A User must exist before generating reports.
- Reports should automatically fetch FoodEntry data linked to the same date.
- If a User is deleted, all reports should also be removed (Cascade Delete).

------------------------------------------------------------------------------------------
MEAL PLAN MODEL (Weekly meal prep tracking)
------------------------------------------------------------------------------------------
Attributes
- id (Primary Key, Unique Identifier)
- user_id (Foreign Key → User.id)
- week_number (Integer, represents the week of the year)
- planned_meals (JSON/String, structured data storing meal prep details)
- nutrition_balance (String, optional, indicates meal nutritional balance e.g., "High Protein, Low Carb")
- created_at (Timestamp, when meal plan was recorded)
- updated_at (Timestamp, tracks last modification)
Relationships
- Many-to-One: Each MealPlan belongs to a User
- One-to-One per Week: A User should have only one active meal plan per week.
- Integrity Rules:
- A User must exist before creating a meal plan.
- If a User is deleted, all MealPlan entries should be removed (Cascade Delete).
