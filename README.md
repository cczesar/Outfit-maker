# Outfit Maker
#### Video Demo:  [<URL HERE>](https://youtu.be/xZgOt6jBwfo)
#### Description:
Outfit maker is a web application designed in a personal style organization for a digital wardrobe management. This web application works as a virtual closet and outfit planning tool, enabling users to digitally catalog their items, use imagination with fashion combinations and save outfits for future. Built on Flask framkework with SQLite database backend, the web application got a modern simple and intuitive interface that make outfits planning practical and simple.

A common problem is not knowing what to wear and not having to much time to try on different outfit, with a interactive platform where users can see their clothing combinations come to life before ever putting them on, outfit maker make the process easy offering flexibility and creativity personal styling.

The main function is allow users to upload images of their clothing items, categorize them in a 4 main sections Upper body, Lower body, Shoes and Accesories. then mix however they want these items on a virtual canvas. Each uploaded items is stored with is image, name and category making it easy to find and organize digital closet.

Demonstrate full-stack web development, combing python flask for backend, SQLite for data, javascript for fronted experience, with this features a drag and drop interface that allows a easy positioning and scaling of items. The canvas got thje function of a automatic canvas capture system generate a preview image of completed outfits, allowing the users see the ouftis saved anytime.

#### The problem it solves:
Management and personal styling. The main problem addressed is the daily struggle of deciding what to wear for limited time or personal problems. By pre-planning outfits digitally, users reduce morning stress and save time for more important things.
One important thing is that many people don't use all of their clothes, forgotten items in ther closets, with Outfit maker can rediscover old items, encouraging users to incorporate pieces into new combinations, maximizing their clothing and reducing the impulse for unnecessary purchases.

Futhermore, Outfit maker solves practical problems. Physical closet space prevent users to see their entire wardrobe at once, leading to always use the same ouftis. The digital closet provides a virtual space, displaying every uploaded item simultaneously and enabling comprehensive wardrobe assessment. This facilities better purchasing decisions and more creative outfit construction.

Users can address the challenger of outfit planning for specific occasions, such as business tralel, vacation or special events, the tool can be use to pre-plan complete ouftis in minutes making it easy to share outfits ideas with family and freinds for feedback.

#### How it Works:

The web application operates through a workflow that begin with uploaded items and progresses through outfit creation to saved and management. Users use their digital closet by uploading items through a simple intuitive interface.
Each item requires categorization into the 4 sections, maintaining organizational focus. The backend involes multiple secuirty measures, including filename and a directory path validation. Uploaded images are stored in a dedicated uploads directory while item data name, category and image-path are in SQLite database.
The system handles path corrections, ensuring proper image rendering regardless of file location.

Once uploaded, items automatically appear in their respective category in a visually grid layout. This employs easy management and usability. Each item displays as a thumbail image with its name.
The categorization make it easier to quick filtering and browsing combinations of items.
The maing thing in Outfit maker is the interactive canvas system where users build outfits on their owen by clicking items thumbnails, which instantly appear on the virtual canvas, this implements a drag and drop function with custom javascript, each draggabale item features a resize button handling a good aspect ratio while allowing making it fit for the ouftit.
The canvas provides a collision detecion and boundary constraints preveting items from extending beyond the limits of the canvas. Layering management ensures selected items always appear on top of other trying to recreate a layering like in real life.
When users complete a outfit they can save it with a name for later, this is tricky where the canvas converts into a base64 encoded png image. This involve creating temporary canvas element and drawing each clothing item with the correct position, scaling and resolution. The result a image working as a visual reference to see what users create and save as a outfit. This automated screenshot genereations eliminates the need for manual saved making it easier and funny to create outfits.

The saved outfits display in a organized list under the canvas as My Outfits(0)
each entry showing the outfit name and its genereated preview image, allow users to open any outfit in a full screen view, the management system includes indiviual outfit delete button with a confirmation button, for a more wardrobe resets theres a "Delete ALL items" in the wardrobe sections making it easy to organize better.

The technical architecture demostrata frontend a backend concerns. The flask application handles routing, file management and database operations while the frontend manage complex user interactions. In operation Outfit maker make easy the process of outfit planning into an enganing, creative activity, making experiment with your wardrobe with infinite posibilities.
By both practical organizational need and creative expression desires. Outfit maker represents a simple tool where it becomes a must in personal style development.

