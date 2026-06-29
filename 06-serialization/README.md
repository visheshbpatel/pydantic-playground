# 06 - Serialization

This project demonstrates how to serialize Pydantic models into Python dictionaries and JSON strings.

Serialization is an important part of working with APIs because data often needs to be converted into formats that can be stored, transmitted, or returned to clients.

---

## What is Serialization?

Serialization is the process of converting a Python object into a format that can be:

- Stored in a file
- Sent over a network
- Returned by an API
- Saved in a database

Pydantic provides built-in methods for serializing models into:

- Python dictionaries
- JSON strings

---

## Concepts Covered

- `model_dump()`
- `model_dump_json()`
- Nested model serialization
- `include`
- `exclude`
- `exclude_unset`
- Default values during serialization
- Dictionary serialization
- JSON serialization

---

## Models Used

### Address Model

```python
class Address(BaseModel):

    city: str
    state: str
    pin: str
```

### Patient Model

```python
class Patient(BaseModel):

    name: str
    gender: str = "Male"
    age: int
    address: Address
```

The `Patient` model contains a nested `Address` model.

---

## Creating a Model Instance

```python
address = Address(
    city="indore",
    state="madhya pradesh",
    pin="454545"
)

patient = Patient(
    name="vishesh",
    age=22,
    address=address
)
```

Notice that:

```python
gender
```

is not provided.

Pydantic automatically uses the default value:

```python
"Male"
```

---

## model_dump()

The `model_dump()` method converts a Pydantic model into a Python dictionary.

Example:

```python
patient.model_dump()
```

Output:

```python
{
    'name': 'vishesh',
    'gender': 'Male',
    'age': 22,
    'address': {
        'city': 'indore',
        'state': 'madhya pradesh',
        'pin': '454545'
    }
}
```

Type:

```python
<class 'dict'>
```

---

## model_dump_json()

The `model_dump_json()` method converts a Pydantic model into a JSON string.

Example:

```python
patient.model_dump_json()
```

Output:

```json
{"name":"vishesh","gender":"Male","age":22,"address":{"city":"indore","state":"madhya pradesh","pin":"454545"}}
```

Type:

```python
<class 'str'>
```

---

## model_dump() vs model_dump_json()

| Method | Output Type |
|----------|----------|
| `model_dump()` | Python Dictionary |
| `model_dump_json()` | JSON String |

---

## Including Specific Fields

The `include` parameter allows serialization of only selected fields.

Example:

```python
patient.model_dump(
    include=['name', 'gender']
)
```

Output:

```python
{
    'name': 'vishesh',
    'gender': 'Male'
}
```

This is useful when only a subset of data needs to be returned.

---

## Excluding Fields

The `exclude` parameter removes specific fields from the serialized output.

Example:

```python
patient.model_dump(
    exclude={'address': ['state']}
)
```

Output:

```python
{
    'name': 'vishesh',
    'gender': 'Male',
    'age': 22,
    'address': {
        'city': 'indore',
        'pin': '454545'
    }
}
```

The nested field:

```python
address.state
```

is excluded from the result.

---

## Excluding Unset Fields

The `exclude_unset=True` parameter removes fields that were not explicitly provided during model creation.

Model:

```python
class Patient(BaseModel):
    gender: str = "Male"
```

Input:

```python
patient = Patient(
    name="vishesh",
    age=22,
    address=address
)
```

Notice that:

```python
gender
```

was not provided.

Pydantic automatically assigned:

```python
"Male"
```

---

Normal serialization:

```python
patient.model_dump()
```

Output:

```python
{
    'name': 'vishesh',
    'gender': 'Male',
    'age': 22,
    'address': {...}
}
```

---

Serialization with:

```python
patient.model_dump(
    exclude_unset=True
)
```

Output:

```python
{
    'name': 'vishesh',
    'age': 22,
    'address': {...}
}
```

The `gender` field is omitted because it was not explicitly set by the user.

---

## Nested Model Serialization

Pydantic automatically serializes nested models.

Example:

```python
patient.model_dump()
```

Result:

```python
{
    'name': 'vishesh',
    'gender': 'Male',
    'age': 22,
    'address': {
        'city': 'indore',
        'state': 'madhya pradesh',
        'pin': '454545'
    }
}
```

The nested `Address` model is converted into a nested dictionary.

---

## Serialization Workflow

### Step 1: Create Model

```python
patient = Patient(...)
```

### Step 2: Serialize

```python
patient.model_dump()
```

or

```python
patient.model_dump_json()
```

### Step 3: Generate Output

```text
Pydantic Model
        ↓
Serialization
        ↓
Dictionary / JSON
```

---

## Real-World Use Cases

Serialization is commonly used for:

### API Responses

```python
return patient
```

### Saving Data

```python
patient.model_dump()
```

### Sending JSON Data

```python
patient.model_dump_json()
```

### Logging and Debugging

```python
print(patient.model_dump())
```

### Database Operations

```python
db.insert(patient.model_dump())
```

---

## Key Takeaways

- Serialization converts models into dictionaries or JSON.
- `model_dump()` returns a Python dictionary.
- `model_dump_json()` returns a JSON string.
- `include` allows selected fields to be serialized.
- `exclude` removes specific fields from the output.
- `exclude_unset=True` removes fields that were not explicitly provided.
- Nested models are automatically serialized.
- Serialization is heavily used in FastAPI APIs and data exchange workflows.