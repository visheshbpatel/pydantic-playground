# 05 - Nested Models

This project demonstrates how to use nested models in Pydantic to represent and validate complex hierarchical data structures.

Nested models allow one Pydantic model to be used as a field inside another model, making it easier to organize related data and maintain clean schemas.

---

## What are Nested Models?

A nested model is a Pydantic model that is used as a field within another Pydantic model.

Instead of storing all data in a single flat model, related data can be grouped into separate reusable models.

Example:

```python
class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    age: int
    address: Address
```

In this example:

- `Address` is a separate model.
- `Patient` contains an `Address` model.
- `Address` becomes a nested model inside `Patient`.

---

## Concepts Covered

- Nested models
- Model composition
- Hierarchical data structures
- Automatic nested validation
- Accessing nested fields
- Reusable schemas
- Data organization
- Nested serialization

---

## Why Use Nested Models?

Consider the following patient data:

```python
{
    "name": "Vishesh",
    "gender": "Male",
    "age": 22,
    "city": "Indore",
    "state": "Madhya Pradesh",
    "pin": "454545"
}
```

As applications grow, models often contain:

- Address information
- Contact information
- Insurance details
- Medical records
- Emergency contacts

Keeping everything in a single model becomes difficult to manage.

A better approach is to group related fields together.

```python
Patient
│
├── Name
├── Gender
├── Age
│
└── Address
     ├── City
     ├── State
     └── Pin
```

This structure is cleaner, reusable, and easier to maintain.

---

## Address Model

The project defines a dedicated model for address information.

```python
class Address(BaseModel):

    city: str
    state: str
    pin: str
```

This model represents:

```text
Address
├── city
├── state
└── pin
```

---

## Patient Model

The patient model contains personal information and a nested address.

```python
class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address
```

Notice:

```python
address: Address
```

The `address` field is not a string or dictionary.

It must be a valid `Address` model.

---

## Creating a Nested Model

### Step 1: Create Address Data

```python
address_dict = {
    "city": "indore",
    "state": "madhya pradesh",
    "pin": "454545"
}
```

---

### Step 2: Create Address Object

```python
address1 = Address(**address_dict)
```

Pydantic validates the address data and creates an `Address` object.

---

### Step 3: Create Patient Data

```python
patient_dict = {
    "name": "vishesh",
    "gender": "male",
    "age": 22,
    "address": address1
}
```

---

### Step 4: Create Patient Object

```python
patient1 = Patient(**patient_dict)
```

Result:

```text
Patient
│
├── name
├── gender
├── age
│
└── address
     ├── city
     ├── state
     └── pin
```

---

## Accessing Nested Fields

Nested fields can be accessed using dot notation.

Example:

```python
patient1.name
```

Output:

```text
vishesh
```

---

Accessing address fields:

```python
patient1.address.city
```

Output:

```text
indore
```

---

```python
patient1.address.pin
```

Output:

```text
454545
```

---

## Automatic Nested Validation

Pydantic validates nested models automatically.

Example:

```python
{
    "city": "indore",
    "state": "madhya pradesh"
}
```

Missing:

```python
pin
```

Result:

```text
ValidationError
address.pin
Field required
```

Nested validation ensures all required fields are present and correctly typed.

---

## Direct Dictionary Support

Pydantic can automatically create nested models from dictionaries.

Instead of:

```python
address = Address(
    city="indore",
    state="madhya pradesh",
    pin="454545"
)

patient = Patient(
    name="vishesh",
    gender="male",
    age=22,
    address=address
)
```

You can directly pass:

```python
patient = Patient(
    name="vishesh",
    gender="male",
    age=22,
    address={
        "city": "indore",
        "state": "madhya pradesh",
        "pin": "454545"
    }
)
```

Pydantic automatically converts the dictionary into an `Address` model.

---

## Validation Workflow

### Step 1: Receive Raw Data

```python
Patient Data
    ↓
Address Data
```

---

### Step 2: Validate Address

```python
Address(
    city,
    state,
    pin
)
```

---

### Step 3: Validate Patient

```python
Patient(
    name,
    gender,
    age,
    address
)
```

---

### Step 4: Create Nested Model

```text
Patient
│
├── name
├── gender
├── age
│
└── address
     ├── city
     ├── state
     └── pin
```

---

## Real-World Use Cases

Nested models are commonly used for:

### User Profiles

```text
User
└── Address
```

---

### E-Commerce

```text
Order
├── Customer
├── Shipping Address
└── Billing Address
```

---

### Healthcare Systems

```text
Patient
├── Address
├── Insurance
└── Emergency Contact
```

---

### Banking Applications

```text
Customer
├── Address
├── Account Details
└── Nominee Information
```

---

## Benefits of Nested Models

- Better organization of related data
- Reusable schemas
- Cleaner code structure
- Automatic nested validation
- Easier maintenance
- Improved readability
- Better API schema generation

---

## Key Takeaways

- A nested model is a Pydantic model used inside another model.
- Nested models help represent hierarchical data structures.
- Pydantic automatically validates nested data.
- Nested fields can be accessed using dot notation.
- Dictionaries can be automatically converted into nested models.
- Nested models improve code organization and reusability.
- They are widely used in FastAPI APIs and real-world applications.
- Complex data structures become easier to manage and validate.