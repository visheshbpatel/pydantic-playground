# 04 - Computed Fields

This project demonstrates how to use Pydantic computed fields to create values that are automatically derived from other model fields.

Computed fields allow developers to expose calculated values as part of a model without requiring those values to be provided by the user.

---

## What are Computed Fields?

A computed field is a field whose value is calculated from other fields in the model.

Instead of storing the value directly, Pydantic computes it whenever it is accessed.

Example:

```python
@computed_field
@property
def bmi(self) -> float:
    return round(self.weight / (self.height ** 2), 2)
```

In this example:

- `weight` and `height` are stored fields.
- `bmi` is a computed field.
- The user does not need to provide a BMI value.

---

## Concepts Covered

- `@computed_field`
- `@property`
- Derived fields
- Dynamic calculations
- Model serialization
- Accessing computed values
- Calculating values from existing fields
- Exposing computed values in API responses

---

## Why Use Computed Fields?

Consider a patient record:

```python
{
    "weight": 65,
    "height": 1.72
}
```

BMI can be calculated using:

```text
BMI = Weight / Height²
```

Instead of requiring users to provide:

```python
{
    "weight": 65,
    "height": 1.72,
    "bmi": 21.97
}
```

the application can calculate BMI automatically.

Benefits:

- Eliminates duplicate data
- Prevents inconsistent values
- Reduces user input requirements
- Keeps business logic centralized

---

## Understanding @property

The `@property` decorator allows a method to behave like an attribute.

Without `@property`:

```python
class Patient:

    def bmi(self):
        return 21.97
```

Access:

```python
patient.bmi()
```

---

With `@property`:

```python
class Patient:

    @property
    def bmi(self):
        return 21.97
```

Access:

```python
patient.bmi
```

The method is executed automatically when the attribute is accessed.

---

## Understanding @computed_field

The `@computed_field` decorator tells Pydantic that the property should be treated as a model field.

Example:

```python
@computed_field
@property
def bmi(self) -> float:
    return round(self.weight / (self.height ** 2), 2)
```

This allows Pydantic to:

- Include the field during serialization
- Expose the field in API responses
- Treat the computed value as part of the model

---

## BMI Calculation

The project calculates BMI using:

```python
bmi = round(
    self.weight / (self.height ** 2),
    2
)
```

Example:

```python
weight = 65
height = 1.72
```

Calculation:

```text
65 / (1.72 × 1.72)
```

Result:

```text
21.97
```

---

## Patient Model

The model stores:

- Name
- Email
- Age
- Weight
- Height
- Marital Status
- Contact Details

The model computes:

- BMI

Example:

```python
class Patient(BaseModel):

    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(
            self.weight / (self.height ** 2),
            2
        )
```

---

## Example Input

```python
patient_info = {
    "name": "vbp",
    "email": "vbp@hdfc.com",
    "age": 65,
    "weight": 65,
    "height": 1.72,
    "married": False,
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

Notice that:

```python
bmi
```

is not provided by the user.

---

## Accessing Computed Fields

Computed fields behave like normal attributes.

Example:

```python
print(patient.bmi)
```

Output:

```text
21.97
```

No parentheses are required because `bmi` is defined using `@property`.

---

## Serialization

Without `@computed_field`, Pydantic does not automatically include properties during serialization.

Example:

```python
patient.model_dump()
```

Without a computed field:

```python
{
    "name": "vbp",
    "weight": 65,
    "height": 1.72
}
```

---

With `@computed_field`:

```python
{
    "name": "vbp",
    "weight": 65,
    "height": 1.72,
    "bmi": 21.97
}
```

This makes computed fields useful in APIs and data export workflows.

---

## Workflow

### Step 1: Receive Input

```python
{
    "weight": 65,
    "height": 1.72
}
```

### Step 2: Create Model

```python
patient = Patient(**patient_info)
```

### Step 3: Access Computed Field

```python
patient.bmi
```

### Step 4: Calculate Value

```python
weight / height²
```

### Step 5: Return Result

```python
21.97
```

---

## Real-World Use Cases

Computed fields are commonly used for:

### BMI

```text
Weight + Height → BMI
```

### Full Name

```text
First Name + Last Name → Full Name
```

### Total Price

```text
Price + Quantity → Total Price
```

### Age

```text
Date of Birth → Age
```

### Order Summary

```text
Order Items → Total Amount
```

---

## Key Takeaways

- Computed fields derive values from existing model fields.
- `@property` allows a method to behave like an attribute.
- `@computed_field` tells Pydantic to treat a property as a model field.
- Computed fields reduce duplicate and inconsistent data.
- Users only provide source data; derived values are calculated automatically.
- Computed fields are included in serialization and API responses.
- They are useful for calculations, summaries, and derived business data.