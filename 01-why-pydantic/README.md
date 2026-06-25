# 01 - Why Pydantic?

This project demonstrates the fundamentals of Pydantic and how it helps validate, parse, and manage structured data in Python applications.

## What is Pydantic?

Pydantic is a data validation library that uses Python type hints to validate, parse, and serialize data.

It helps ensure that incoming data follows a predefined schema before it is used by the application.

### Why Use Pydantic?

Without Pydantic, developers often need to write manual validation code:

```python
if age <= 0:
    raise ValueError("Age must be positive")

if '@' not in email:
    raise ValueError("Invalid email")
```

As applications grow, these checks become repetitive and difficult to maintain.

Pydantic solves this problem by allowing developers to define a schema once and automatically validate incoming data.

```text
Raw Data
    ↓
Pydantic Validation
    ↓
Trusted Python Object
    ↓
Application Logic
```

This reduces bugs, improves data quality, and makes applications easier to maintain.

---

## Concepts Covered

* Creating models using `BaseModel`
* Type validation
* Type coercion
* Field constraints using `Field()`
* Using `Annotated` for validation metadata
* Built-in Pydantic types:

  * `EmailStr`
  * `AnyUrl`
* Optional fields
* List validation
* Dictionary validation
* Default values
* Model instantiation and validation

---

## Concepts Explained

### BaseModel

`BaseModel` is the foundation of Pydantic.

Any class that inherits from `BaseModel` gains:

* Automatic validation
* Type checking
* Type conversion
* Serialization support
* Helpful validation errors

Example:

```python
class User(BaseModel):
    name: str
    age: int
```

When an object is created, Pydantic validates the provided data against the schema.

---

### Field()

`Field()` is used to add validation rules and metadata to model fields.

Example:

```python
age: int = Field(gt=0, lt=120)
```

This ensures that:

```text
0 < age < 120
```

Common constraints:

| Constraint   | Meaning                  |
| ------------ | ------------------------ |
| `gt`         | Greater than             |
| `ge`         | Greater than or equal to |
| `lt`         | Less than                |
| `le`         | Less than or equal to    |
| `min_length` | Minimum length           |
| `max_length` | Maximum length           |

`Field()` can also be used to add:

* Descriptions
* Examples
* Titles
* Default values

---

### Annotated

`Annotated` allows metadata to be attached to a type.

Example:

```python
name: Annotated[str, Field(max_length=50)]
```

This means:

* The field type is `str`
* Maximum length allowed is 50 characters

In Pydantic v2, `Annotated` is the recommended way to combine type hints with validation metadata.

---

### EmailStr

`EmailStr` is a special Pydantic type that validates email addresses.

Example:

```python
email: EmailStr
```

Valid:

```python
"user@gmail.com"
```

Invalid:

```python
"usergmail.com"
```

---

### AnyUrl

`AnyUrl` is a special Pydantic type used for URL validation.

Example:

```python
hospital_url: AnyUrl
```

Valid:

```python
"https://www.apollohospitals.com"
```

Invalid:

```python
"apollohospitals.com"
```

---

### Optional

`Optional[T]` means a field can store either:

* A value of type `T`
* `None`

Example:

```python
married: Optional[bool]
```

Valid values:

```python
True
False
None
```

---

### Type Coercion

One of Pydantic's most useful features is automatic type conversion.

Example:

```python
age = "22"
```

Pydantic can convert it into:

```python
age = 22
```

during validation.

This behaviour can be controlled using strict validation rules when needed.

---

## Patient Model

The project defines a `Patient` schema containing:

* Name
* Email
* Hospital URL
* Age
* Weight
* Marital Status
* Allergies
* Contact Details

Each field includes appropriate type annotations and validation rules.

### Example

```python
patient = Patient(
    name="Vishesh",
    email="vbp@gmail.com",
    hospital_url="https://www.apollohospitals.com",
    age=22,
    weight=65.0,
    contact_details={"phone": "7897897897"}
)
```

---

## Validation Examples

### Valid Data

```python
{
    "name": "Vishesh",
    "email": "user@gmail.com",
    "hospital_url": "https://www.apollohospitals.com",
    "age": 22,
    "weight": 65.0
}
```

### Invalid Data

```python
{
    "email": "invalid-email",
    "hospital_url": "not-a-url",
    "age": -10,
    "weight": -5
}
```

Pydantic automatically raises a `ValidationError` when invalid data is provided.

---

## Project Workflow

The typical workflow when using Pydantic is:

### Step 1: Define a Model

```python
class Patient(BaseModel):
    name: str
    age: int
```

### Step 2: Pass Raw Data

```python
patient = Patient(**patient_data)
```

### Step 3: Validate and Convert

Pydantic:

* Checks required fields
* Validates data types
* Applies constraints
* Converts compatible values

### Step 4: Use Trusted Data

```python
insert_patient_data(patient)
```

Application logic now works with validated and trusted data.

---

## Installation

Install Pydantic and email validation support:

```bash
pip install pydantic[email]
```

---


