# Pydantic Playground

A hands-on learning repository for understanding Pydantic through practical examples.

This repository contains small, focused projects that demonstrate core Pydantic concepts including data validation, custom validators, computed fields, nested models, and serialization.

The goal is to build a strong understanding of how Pydantic works internally and how it is commonly used in modern Python applications and FastAPI projects.

---

## What is Pydantic?

Pydantic is a data validation and parsing library for Python that uses type hints to define schemas and validate incoming data.

It helps developers:

- Validate input data
- Parse raw data into Python objects
- Enforce business rules
- Serialize models into dictionaries and JSON
- Build reliable APIs with FastAPI


---

## Topics Covered

### 01 - Why Pydantic?

Introduction to Pydantic and its role in data validation.

Concepts covered:

- BaseModel
- Type validation
- Type coercion
- Field constraints
- EmailStr
- AnyUrl
- Optional fields
- Dictionary and list validation

---

### 02 - Field Validators

Learn how to implement custom validation logic for individual fields.

Concepts covered:

- field_validator
- Before validators
- After validators
- Data transformation
- Custom business rules
- Validation errors

---

### 03 - Model Validators

Learn how to validate an entire model using cross-field validation.

Concepts covered:

- model_validator
- Model-level validation
- Cross-field validation
- Business rule enforcement
- Validation lifecycle

---

### 04 - Computed Fields

Learn how to create dynamically calculated fields.

Concepts covered:

- computed_field
- property
- Derived values
- Dynamic calculations
- Model serialization

Example:

```text
Weight + Height
        ↓
       BMI
```

---

### 05 - Nested Models

Learn how to create hierarchical and reusable schemas.

Concepts covered:

- Nested models
- Model composition
- Nested validation
- Nested serialization
- Structured data modeling

Example:

```text
Patient
│
└── Address
    ├── City
    ├── State
    └── Pin
```

---

### 06 - Serialization

Learn how to convert models into dictionaries and JSON.

Concepts covered:

- model_dump()
- model_dump_json()
- include
- exclude
- exclude_unset
- Nested serialization

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install Pydantic:

```bash
pip install pydantic[email]
```

---

## Learning Path

For the best experience, follow the projects in order:

```text
01 - Why Pydantic
        ↓
02 - Field Validators
        ↓
03 - Model Validators
        ↓
04 - Computed Fields
        ↓
05 - Nested Models
        ↓
06 - Serialization
```

Each project builds upon concepts introduced in previous sections.

---

## Key Takeaways

- Pydantic uses Python type hints for validation.
- BaseModel provides automatic parsing and validation.
- Field validators handle field-specific rules.
- Model validators handle cross-field validation.
- Computed fields derive values dynamically.
- Nested models represent hierarchical data.
- Serialization converts models into dictionaries and JSON.
- Pydantic is a foundational component of FastAPI applications.

---

## Author

**Vishesh Patel**

Exploring Pydantic through hands-on projects, practical examples, and detailed documentation.