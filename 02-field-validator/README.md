# 02 - Field Validators

This project demonstrates how to use Pydantic field validators to implement custom validation and data transformation logic.

While `Field()` is useful for applying generic validation rules such as ranges and length constraints, `field_validator()` allows developers to enforce business-specific rules and modify incoming data during the validation process.

---

## What are Field Validators?

Field validators are custom functions that run automatically when a model is being validated.

They allow you to:

- Validate field values using custom logic
- Transform incoming data before validation
- Perform additional checks after validation
- Enforce business rules that cannot be expressed using `Field()`

Example:

```python
@field_validator('email')
@classmethod
def validate_email(cls, value):
    if not value.endswith("@company.com"):
        raise ValueError("Invalid company email")
    return value
```

---

## Concepts Covered

- `@field_validator`
- Custom validation logic
- Validation lifecycle
- `mode="before"`
- `mode="after"`
- Data transformation
- Business rule validation
- Raising validation errors
- Type coercion and validators
- Multiple validation layers

---

## Why Use Field Validators?

Basic validation rules can be handled using `Field()`.

Example:

```python
age: int = Field(gt=0, lt=120)
```

However, some requirements are application-specific:

- Only certain email domains are allowed
- Names should be formatted consistently
- Age should follow additional business rules
- Data should be cleaned before storage

These scenarios require custom validators.

---

## Validation Flow

When a model instance is created, Pydantic performs validation in multiple stages.

```text
Raw Input
    ↓
Before Validators
    ↓
Type Conversion
    ↓
Field Validation
    ↓
After Validators
    ↓
Model Created
```

Example:

```python
patient = Patient(**patient_data)
```

During this step, all validators are executed automatically.

---

## Email Domain Validation

The project validates that email addresses belong to approved domains.

```python
@field_validator('email')
@classmethod
def email_validator(cls, value):

    valid_domain = ['hdfc.com', 'icici.com']
    domain_name = value.split('@')[-1]

    if domain_name not in valid_domain:
        raise ValueError('Not a valid domain')

    return value
```

### Valid Examples

```text
user@hdfc.com
user@icici.com
```

### Invalid Examples

```text
user@gmail.com
user@yahoo.com
```

If an invalid domain is provided, Pydantic raises a `ValidationError`.

---

## Before Validators

A validator with `mode="before"` runs before normal Pydantic validation.

Example:

```python
@field_validator('name', mode='before')
@classmethod
def transform_name(cls, value):
    return value.capitalize()
```

Input:

```python
"name": "vbp"
```

Output:

```python
"Vbp"
```

### Use Cases

- Cleaning whitespace
- Formatting names
- Converting input formats
- Standardizing data before validation

---

## After Validators

A validator with `mode="after"` runs after type conversion and field validation.

Example:

```python
@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):

    if 0 < value < 100:
        return value

    raise ValueError("Age should be between 0 and 100")
```

Input:

```python
"22"
```

Pydantic first converts:

```python
22
```

Then the validator executes.

### Use Cases

- Business rule validation
- Cross-checking processed values
- Additional restrictions after conversion

---

## Understanding @classmethod

Field validators are defined as class methods.

```python
@field_validator('email')
@classmethod
def email_validator(cls, value):
```

### Why?

Validation happens before the model instance is fully created.

At validation time:

```text
Raw Data
    ↓
Validation
    ↓
Model Instance Created
```

Since the object does not yet exist, validators cannot use `self`.

Instead, Pydantic executes validators at the class level using `cls`.

---

## Type Coercion and Validators

Pydantic automatically converts compatible values during validation.

Input:

```python
{
    "age": "22"
}
```

Schema:

```python
age: int
```

Result:

```python
age = 22
```

After conversion, the age validator executes.

---

## Model Fields

The `Patient` model includes:

- Name
- Email
- GitHub URL
- Age
- Weight
- Marital Status
- Allergies
- Contact Details

The model combines:

- Built-in validation
- Field constraints
- Custom field validators

to create a robust validation system.

---

## Example Input

```python
patient_info = {
    "name": "vbp",
    "email": "vbp@hdfc.com",
    "github_url": "https://github.com/visheshbpatel",
    "age": "22",
    "weight": 65,
    "contact_details": {
        "phone": 789789
    }
}
```

Creating the model:

```python
patient = Patient(**patient_info)
```

Pydantic will:

1. Transform the name
2. Validate the email domain
3. Validate the GitHub URL
4. Convert age to an integer
5. Validate age rules
6. Validate weight constraints
7. Validate contact details
8. Create the final model instance

---

## Validation Errors

When validation fails, Pydantic raises a `ValidationError`.

Example:

```python
{
    "email": "user@gmail.com"
}
```

Output:

```text
Value error, Not a valid domain
```

Validation errors help identify invalid input before it reaches application logic.

---

## Key Takeaways

- `Field()` handles generic validation rules.
- `field_validator()` handles custom business logic.
- `mode="before"` runs before normal validation.
- `mode="after"` runs after validation and type conversion.
- Validators can transform incoming data.
- Validators can enforce domain-specific rules.
- Pydantic automatically raises validation errors when checks fail.
- Field validators make models cleaner, reusable, and easier to maintain.