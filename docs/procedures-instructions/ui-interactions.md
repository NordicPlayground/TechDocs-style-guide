# Describing interactions with UI

Customers interact with products using different input methods: keyboard, mouse, touch, voice, and more. So use generic verbs that work with any input method. Don't use input-specific verbs, such as *click* or *swipe*. Instead, use the verbs listed here.

| **Verb** | **Use for** | **Examples** |
|----------|-------------|--------------|
| **Open** | <ul><li>Apps and programs</li></ul><ul><li>Blades</li></ul><ul><li>File Explorer</li></ul><ul><li>Files and folders</li></ul><ul><li>Shortcut menus</li></ul><ul><li>Use for websites and webpages only when necessary to match the UI. Otherwise, use *go to*.</li></ul><ul><li>Don't use for commands and menus.</li></ul> | <ul><li>Open Photos.</li></ul><ul><li>Open the Reader app.</li></ul><ul><li>Select **Users + groups** to open the blade.</li></ul><ul><li>Open the Filename file.</li></ul><ul><li>To open the document in Outline view, select **View > Outline**.</li></ul><ul><li>In WindowName, open the shortcut menu for ItemName.</li></ul> |
| **Close** | <ul><li>Apps and programs</li></ul><ul><li>Blades</li></ul><ul><li>Dialog boxes</li></ul><ul><li>Files and folders</li></ul><ul><li>Notifications and alerts</li></ul><ul><li>Tabs</li></ul><ul><li>The action a program or app takes when it encounters a problem and can't continue. (Don't confuse with *stop responding*.)</li></ul> | <ul><li>Close the Alarms app.</li></ul><ul><li>Close Excel.</li></ul><ul><li>Close the blade.</li></ul><ul><li>Close the **Users + groups** blade.</li></ul><ul><li>Save and close the document.</li></ul><ul><li>Closing Excel also closes all open worksheets.</li></ul> |
| **Leave** | Websites and webpages | Select **Submit** to complete the survey and leave this page. |
| **Go to** | <ul><li>Opening a menu.</li></ul><ul><li>Going to a tab or another particular place in the UI.</li></ul><ul><li>Going to a website or webpage.</li></ul><ul><li>It's OK to use *On the* **XXX** *tab* if the instruction is brief and continues immediately.</li></ul> | <ul><li>Go to Search <img src="media/describing-interactions-with-ui/721771267.png"/> , enter the word **settings**, and then select **Settings**.</li></ul><ul><li>Go to **File**, and then select **Close**.</li></ul><ul><li>On the ribbon, go to the **Design** tab.</li></ul><ul><li>Go to the **Deploy** tab. In the **Configuration** list …</li></ul><ul><li>On the **Deploy** tab, in the **Configuration** list …</li></ul><ul><li>Go to Example.com to register.</li></ul> |
| **Select** | Instructing the customer to select a specific item:<br/><ul><li>Selecting an option, such as a button.</li></ul><ul><li>Selecting a check box.</li></ul><ul><li>Selecting a value from a list box.</li></ul><ul><li>Selecting link text to go to a link.</li></ul><ul><li>Selecting an item on a menu or shortcut menu.</li></ul><ul><li>Selecting an item from a gallery.</li></ul><ul><li>Selecting keys and keyboard shortcuts. (Document keyboard shortcuts only if they're the most likely way the customer will accomplish a task or as an alternative input method, usually in a separate keyboard shortcuts article.)</li></ul> | <ul><li>Select the **Modify** button.</li></ul><ul><li>For **Alignment**, select **Left**.</li></ul><ul><li>Select the text, open the shortcut menu, and then select **Font**.</li></ul><ul><li>Select **Open in new tab**.</li></ul><ul><li>Select the **LinkName** link.</li></ul><ul><li>Select **F5**.</li></ul><ul><li>Select **Shift+Enter**.</li></ul><ul><li>Select **Ctrl+Alt+Delete**.</li></ul> |
| **Select and hold, select and hold (or right-click)** | Use to describe pressing and holding an element in the UI. It's OK to use *right-click* with *select and hold* when the instruction isn't specific to touch devices. | <ul><li>To flag a message that you want to deal with later, select and hold it, and then select **Set flag**.</li></ul><ul><li>Select and hold (or right-click) the Windows taskbar, and then select **Cascade windows**.</li></ul><ul><li>Select and hold (or right-click) the **Start** <img src="media/describing-interactions-with-ui/967781121.png"/> button, and then select **Device Manager**.</li></ul> |
| **>** | Use a greater-than symbol (>) to separate sequential steps. Only use this approach when there's a clear and obvious path through the UI and the selection method is the same for each step. For example, don't mix things that require opening, selecting, and choosing. Don't bold the greater-than symbol. Include a space before and after the symbol. | Select **Accounts > Other accounts > Add an account**. |
| **Clear** | Clearing the selection from a check box. | Clear the **Header row** check box. |
| **Choose** | Choosing an option based on the customer's preference or desired outcome. | On the **Font** tab, choose the effects you want. |
| **Switch, turn on, turn off** | Turning a toggle key or toggle switch on or off. | <ul><li>Use the **Caps lock** key to switch from typing capital letters to typing lowercase letters.</li></ul><ul><li>To switch between Normal, Outline, and Slide Sorter views, use the buttons on the **View** tab.</li></ul><ul><li>To make text and apps easier to see, turn on the toggle under **Turn on high contrast**.</li></ul><ul><li>To keep all applied filters, turn on the **Pass all filters** toggle.</li></ul> |
| **Enter** | Instructing the customer to type or otherwise insert a value or to type/select a value in a combo box. | <ul><li>In the search box, enter…</li></ul><ul><li>In the **Tab stop position** box, enter the location where you want to set the new tab.</li></ul><ul><li>In the **Deployment script name** box, enter a name for this script.</li></ul> |
| **Move, drag** | Moving anything from one place to another by dragging, cutting and pasting, or another method. Use for tiles and any open window (including apps, dialog boxes, files, and blades). Use *move through* to describe moving around on a page, through screens/pages in an app, or up, down, right, and left in a UI. | <ul><li>Drag the Filename file to the Foldername folder.</li></ul><ul><li>Move the tile to the new section.</li></ul><ul><li>Drag the Snipping Tool out of the way if necessary, and then select the area you want to capture.</li></ul><ul><li>If the **Apply Styles** task pane is in your way, just move it.</li></ul> |
| **Zoom, zoom in, zoom out** | Use *zoom,* *zoom in,* and *zoom out* to refer to changing the magnification of the screen or window. | <ul><li>Zoom in to see more details on the map.</li></ul><ul><li>Zoom out to see a larger geographic area on the map.</li></ul><ul><li>Zoom in or out to see more or less detail.</li></ul> |

## Markdown GUI documentation guidelines

When documenting graphical user interfaces, follow these principles to create clear, consistent instructions.

### Identify UI elements accurately

Use the exact text or label as it appears in the interface. Match capitalization and punctuation.

**Examples:**

* Button says "Add Device" → Write: Click **Add Device**
* Tab says "Configuration" → Write: On the **Configuration** tab
* Field labeled "Device Name:" → Write: In the **Device Name** field

### Format UI elements consistently

Use consistent formatting to help users quickly identify UI elements.

**Bold for clickable elements:**

* **Buttons:** Click **Save**
* **Menus:** On the **File** menu
* **Tabs:** Select the **Advanced** tab

**Italics for values:**

* Enter *MyDevice* in the **Name** field

### Document menu paths clearly

Use the greater-than symbol (>) to show menu navigation paths.

**Format:** Menu > Submenu > Command

**Examples:**

* Select **File** > **Open** > **Project**
* Go to **Tools** > **Options** > **Advanced**

## Screen capture guidelines

Use screen captures strategically to enhance documentation.

### When to use screen captures

**Use for:**

* Complex UIs difficult to describe
* Showing exact location of UI elements
* Illustrating Before/After states

**Don't use for:**

* Simple actions ("Click **OK**")
* UIs that change frequently

## UI element terminology

Use consistent terminology for UI elements.

| **Element Type** | **Preferred Term** | **Examples** |
| ---------------- | ------------------ | ------------ |
| Push button | button | Click the **Add** button |
| Toggle button | toggle, switch | Turn on the **Enable BLE** toggle |
| Checkbox | checkbox | Select the **Show advanced options** checkbox |
| Dropdown | list, dropdown list | From the **Board** list, select your board |
| Text field | field, text box | In the **Device Name** field, enter a name |
| Tab | tab | On the **Configuration** tab |
| Menu | menu | From the **File** menu |
| Dialog box | dialog, dialog box | The **Settings** dialog opens |
| Window | window | Close the **Device Manager** window |

### Nordic-specific terminology

* Use "app" not "application": "Open the Programmer app"
* Use "DK" consistently: "Connect the nRF52840 DK"
* Use specific button names: "Press **Button 1**"

## Documenting menus, dialogs, and wizards

### Menus

**Simple selections:**

"Select **File** > **Save**"

### Dialog boxes

**Opening:**

"Click **Settings** to open the Settings dialog"

**Steps within:**

1. In the **Device Name** field, enter a name
2. From the **Connection Type** list, select **BLE**
3. Click **OK**

### Wizards

Format as numbered steps with each page as a step:

1. On the **Welcome** page, click **Next**
2. On the **Device Selection** page, select your device and click **Next**
3. On the **Configuration** page, configure settings and click **Finish**
