# TechDocs Style Guide

This style guide is forked from the [Microsoft Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide/tree/main/styleguide). We will gradually be updating and adapting the content to suit the needs of Nordic.

The purpose of this style guide is to be a resource to train internal AI models as well as have an updated digital style guide for easier reference and CI check integration.

## MkDocs framework

We use a combination of the [MkDocs framework](https://www.mkdocs.org) with the [Material](https://squidfunk.github.io/mkdocs-material) theme to build the static documentation site.

## Best Way to View the Style Guide Without Causing Conflicts with NCS Requirements

### Step 1: Create a Folder for the Virtual Environment
Create a folder to contain the Virtual Environment.

### Step 2: Create a Python Virtual Environment
Run the following command to create a Virtual Environment in the folder:

```bash
python -m venv NewVenvName
```

### Step 3: Activate the Virtual Environment
- **On Windows:**
  ```bash
  NewVenvName\Scripts\activate
  ```
- **On Linux:**
  ```bash
  source NewVenvName/bin/activate
  ```

### Step 4: Set up the framework inside the Python Virtual Environment
You will need `pip` to install both MkDocs and Material.

1. Run `pip install mkdocs` to install MkDocs on your machine.
1. Run `pip install mkdocs-material` to install the Material theme.
2. Run `pip install mkdocs-macros-plugin` to install the Macros plugin.

### Step 5: Deactivate the Virtual Environment
To deactivate the Virtual Environment, run:

```bash
deactivate
```
or
```bash
exit
```

---

## Step 6: Clone the Repository
1. Create a folder for cloning the repository in a location of your choice.
2. Navigate to the folder and run:

   ```bash
   git clone https://github.com/NordicPlayground/test-style-guide
   ```

---

## Step 7: Run Mkdocs and preview documentation
1. Navigate to the Virtual Environment folder and activate the Virtual Environment:
   - **On Windows:**
     ```bash
     (Path_to_VE)\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source bin/activate


2. To preview the documentation site while you work in real time, use `mkdocs serve` from the Terminal.
   The site will be previewable on your local server at `127.0.0.1:8000`.
   Press Ctrl+C to shut down the local server.


