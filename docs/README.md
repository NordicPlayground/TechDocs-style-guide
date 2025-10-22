# TechDocs Style Guide

This style guide is forked from the [Microsoft Style Guide](https://github.com/MicrosoftDocs/microsoft-style-guide/tree/main/styleguide). This repo will gradually diverge from upstream as needed.

The purpose of this style guide is to have an updated digital style guide for easier reference and future automation integration.

## MkDocs framework

We use a combination of the [MkDocs framework](https://www.mkdocs.org) with the [Material](https://squidfunk.github.io/mkdocs-material) theme to build the static documentation site.

## How to view the style guide without causing conflicts with NCS requirements

### Step 1: Create a folder for the virtual environment
Create a folder to contain the virtual environment.

### Step 2: Create a python virtual environment
Run the following command to create a virtual environment in the folder:

```bash
python -m venv NewVenvName
```

### Step 3: Activate the virtual environment
- **On Windows:**
  ```bash
  NewVenvName\Scripts\activate
  ```
- **On Linux:**
  ```bash
  source NewVenvName/bin/activate
  ```

### Step 4: Set up the framework inside the python virtual environment
You will need `pip` to install both MkDocs and Material.

1. Run `pip install mkdocs` to install MkDocs on your machine.
1. Run `pip install mkdocs-material` to install the Material theme.
2. Run `pip install mkdocs-macros-plugin` to install the Macros plugin.

### Step 5: Deactivate the virtual environment
To deactivate the Virtual Environment, run:

```bash
deactivate
```
or
```bash
exit
```

---

## Step 6: Clone the repository
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


