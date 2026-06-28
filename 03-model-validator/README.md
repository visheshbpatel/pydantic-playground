# 03 - Model Validators

This project demonstrates how to use Pydantic model validators to implement validation rules that depend on multiple fields.

While `field_validator()` is used to validate individual fields, `model_validator()` allows validation of the entire model after all fields have been processed.

This is useful when business rules depend on relationships between multiple fields.

---

## What is a Model Validator?

A model validator is a custom validation function that operates on the entire model rather than a single field.

It is used when validation logic requires access to multiple fields at the same time.

Example:

```python
@model_validator(mode='after')
def validate_model(self):

    if self.age > 60 and 'emergency' not in self.contact_details:
        raise ValueError("Emergency contact required")

    return self
```

---

## Concepts Covered

- `@model_validator`
- Model-level validation
- Cross-field validation
- Business rule validation
- Validation lifecycle
- `mode="after"`
- Accessing multiple fields during validation
- Combining field validators and model validators

---

## Why Use Model Validators?

Field validators only have access to a single field.

Example:

```python
@field_validator('age')
```

can validate:

```python
age
```

but cannot easily determine:

```python
contact_details
```

Similarly:

```python
@field_validator('contact_details')
```

cannot directly validate conditions based on:

```python
age
```

When validation depends on multiple fields together, a model validator is required.

---

## Field Validator vs Model Validator

### Field Validator

Validates a single field.

Example:

```python
@field_validator('email')
```

Use cases:

- Email validation
- Name formatting
- Age range validation
- Data transformation

---

### Model Validator

Validates the complete model.

Example:

```python
@model_validator(mode='after')
```

Use cases:

- Emergency contact requirements
- Guardian information for minors
- Password confirmation checks
- Conditional field requirements

---

## Validation Flow

Pydantic performs validation in multiple stages.

```text
Raw Input
    ↓
Before Field Validators
    ↓
Type Conversion
    ↓
Field Constraints
    ↓
After Field Validators
    ↓
Model Instance Created
    ↓
Model Validators
    ↓
Final Validated Object
```

---

## Emergency Contact Validation

The project includes a business rule:

> Patients older than 60 years must provide an emergency contact.

Implementation:

```python
@model_validator(mode='after')
def validate_emergency_contact(self):

    if self.age > 60 and 'emergency' not in self.contact_details:
        raise ValueError(
            "Patients older than 60 must have an emergency contact"
        )

    return self
```

---

## How It Works

Consider the following data:

```python
{
    "age": 65,
    "contact_details": {
        "phone": 789789
    }
}
```

Validation logic:

```python
age > 60
```

Result:

```python
True
```

Check:

```python
'emergency' not in contact_details
```

Result:

```python
True
```

Validation fails and a `ValidationError` is raised.

---

## Valid Example

```python
{
    "age": 65,
    "contact_details": {
        "phone": 789789,
        "emergency": 898989
    }
}
```

Validation passes because the required emergency contact is present.

---

## Why Use mode="after"?

The validator needs access to:

```python
self.age
self.contact_details
```

These values are only available after:

- Type conversion
- Field validation
- Model creation

have already been completed.

Therefore:

```python
@model_validator(mode='after')
```

is used.

---

## Combining Field Validators and Model Validators

The project uses both validation approaches.

### Field Validators

```python
@field_validator('email')
```

Validates approved email domains.

```python
@field_validator('name', mode='before')
```

Formats the patient's name.

```python
@field_validator('age')
```

Applies custom age validation.

---

### Model Validator

```python
@model_validator(mode='after')
```

Ensures elderly patients have an emergency contact.

This demonstrates how model validators complement field validators rather than replace them.

---

## Example Input

```python
patient_info = {
    "name": "vbp",
    "email": "vbp@hdfc.com",
    "github_url": "https://github.com/visheshbpatel",
    "age": "65",
    "weight": 65,
    "contact_details": {
        "phone": 789789,
        "emergency": 898989
    }
}
```

Creating the model:

```python
patient = Patient(**patient_info)
```

---

## Complete Validation Process

Pydantic performs the following steps:

### Step 1: Name Transformation

```python
"vbp"
```

↓

```python
"Vbp"
```

---

### Step 2: Email Validation

Checks:

- Email format
- Approved email domain

---

### Step 3: URL Validation

Validates:

```python
github_url
```

using `AnyUrl`.

---

### Step 4: Type Conversion

Converts:

```python
"65"
```

↓

```python
65
```

---

### Step 5: Field Validation

Validates:

- Age range
- Weight constraints
- Contact details structure

---

### Step 6: Model Validation

Checks:

```python
age > 60
```

and

```python
'emergency' in contact_details
```

---

### Step 7: Create Final Model

A fully validated `Patient` object is returned.

---

## Validation Errors

If an elderly patient does not provide an emergency contact:

```python
{
    "age": 65,
    "contact_details": {
        "phone": 789789
    }
}
```

Pydantic raises:

```text
Value error, Patients older than 60 must have an emergency contact
```

This prevents invalid data from reaching application logic.

---

## Key Takeaways

- `field_validator()` validates individual fields.
- `model_validator()` validates the entire model.
- Model validators are useful for cross-field validation.
- Business rules often require access to multiple fields.
- `mode="after"` runs after the model has been created.
- Model validators help enforce real-world application rules.
- Field validators and model validators are often used together.
- Pydantic automatically raises validation errors when model-level rules fail.