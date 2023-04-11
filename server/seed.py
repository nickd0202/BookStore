from random import choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, User, Book, Review, Quote

with app.app_context():

    print("Deleting data...")
    User.query.delete()
    Book.query.delete()
    Review.query.delete()
    Quote.query.delete()

    print("Starting seed...")

    print("Creating Users...")

    user1 = User(username = "Chris", age = 21)
    user2 = User(username = "Justin", age = 35)
    user3 = User(username = "Ayah", age = 32)
    user4 = User(username = "Robert", age = 54)
    user5 = User(username = "Nate", age = 27)
    user6 = User(username = "Isabella", age = 30)

    users = [user1,user2,user3,user4,user5,user6]
        
    print("Creating Books...")
    book1 = Book(name ="1984", author = "George Orwell", genre = "Dystopian Fiction", publishDate = "1949" , link="https://www.amazon.com/1984-Signet-Classics-George-Orwell/dp/0451524934/ref=sr_1_2?crid=RLJ13HFXNYIK&keywords=1984&qid=1681233471&sprefix=1984%2Caps%2C114&sr=8-2", summary="Set in a dystopian future, 1984 follows the story of Winston Smith, a low-ranking member of the ruling Party, as he begins to question the oppressive government and its leader, Big Brother. Through its depiction of government surveillance, propaganda, and thought control, 1984 remains a cautionary tale about the dangers of totalitarianism and the importance of individual freedom." ,image="https://kbimages1-a.akamaihd.net/c9472126-7f96-402d-ba57-5ba4c0f4b238/353/569/90/False/nineteen-eighty-four-1984-george.jpg")

    book2 = Book(name = "To Kill a Mockingbird", author = "Harper Lee", genre = "Bildungsroman/Southern Gothic", publishDate = "1960", link="https://www.amazon.com/Kill-Mockingbird-Harper-Lee/dp/0446310786",summary="This classic novel explores themes of racism, injustice, and childhood innocence in the small town of Maycomb, Alabama. Through the eyes of young Scout Finch, readers witness the trial of a black man accused of rape and the deep-seated prejudices of the townspeople. With its memorable characters and timeless message, To Kill a Mockingbird is a must-read for all." ,image="https://target.scene7.com/is/image/Target/GUEST_1607358e-8a84-4160-b93f-15b30b146a9f?wid=488&hei=488&fmt=pjpeg")

    book3 = Book(name = "The Catcher in the Rye", author = "J.D. Salinger", genre = "Bildungsroman", publishDate = "1951" ,link="https://www.amazon.com/Catcher-Rye-J-D-Salinger/dp/0316769177/ref=sr_1_1?crid=24TM4507DG093&keywords=catcher+and+the+reebok&qid=1681233785&s=books&sprefix=catcher+and+the+rebook%2Cstripbooks%2C76&sr=1-1" ,summary="This influential novel follows the teenage protagonist, Holden Caulfield, as he navigates his way through a world he sees as phony and full of hypocrisy. Through Holden's journey, Salinger explores themes of innocence, alienation, and rebellion. With its distinctive voice and lasting impact on popular culture, The Catcher in the Rye is a seminal work of American literature." ,image="https://media.npr.org/assets/artslife/books/2009/10/catcher_custom-853c2f7a4f9f9acaa8647dfdc7b9796555ad54a2-s1100-c50.jpg")

    book4 = Book(name = "The Great Gatsby", author = "F. Scott Fitzgerald", genre = "Jazz Age Novel", publishDate = "1925", link="https://www.amazon.com/Great-Gatsby-Original-Fitzgerald-Classic/dp/B0BF3P5XZS/ref=sr_1_1?crid=2XXMA6Y9WSVB9&keywords=great+gatsby+book&qid=1681233589&s=books&sprefix=great+%2Cstripbooks%2C82&sr=1-1", summary="Set in the Roaring Twenties, The Great Gatsby follows the tragic story of Jay Gatsby, a wealthy but mysterious man who is obsessed with his lost love, Daisy Buchanan. Through Gatsby's pursuit of the American Dream, Fitzgerald critiques the shallow materialism and corruption of the era. With its vivid prose and complex characters, The Great Gatsby is a masterful portrayal of a bygone era." ,image="https://m.media-amazon.com/images/I/71FTb9X6wsL._AC_UF1000,1000_QL80_.jpg")

    book5 = Book(name = "Pride and Prejudice", author = "Jane Austen", genre = "Regency Novel", publishDate = "1813", link="https://www.amazon.com/Pride-Prejudice-Original-Austen-Classics/dp/B09XSV5VM8/ref=sr_1_2_sspa?crid=2XTC5EXPAIB01&keywords=pride+and+prejudice+book&qid=1681233649&s=books&sprefix=pride+and+prejudice+book%2Cstripbooks%2C102&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFZVVMyTkZYUzNMNDUmZW5jcnlwdGVkSWQ9QTA2Nzg1NjkzSTQ4U0ZaQ1NTNjRKJmVuY3J5cHRlZEFkSWQ9QTEwMjE1NTExUlpXRU9STjhVVjVXJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", summary="This classic novel follows the romantic entanglements of the Bennet family, particularly the headstrong Elizabeth Bennet and the proud Mr. Darcy. Austen's sharp wit and social commentary provide a humorous yet insightful look into the society of 19th century England. With its enduring characters and themes of love and class, Pride and Prejudice is a timeless masterpiece." ,image="https://m.media-amazon.com/images/I/5176rSnUxfL.jpg")

    book6 = Book(name = "One Hundred Years of Solitude", author = "Gabriel García Márquez", genre = "Magical Realism", publishDate = "1967", link="https://www.amazon.com/Hundred-Solitude-Harper-Perennial-Classics/dp/0060883286/ref=sr_1_1?crid=3OS0D90IG9IZ8&keywords=100+years+of+solitude+book&qid=1681233706&s=books&sprefix=100+years+of+solitude+book%2Cstripbooks%2C110&sr=1-1", summary="This epic novel chronicles the history of the Buendia family and the fictional town of Macondo over the course of one hundred years. Through magical realism and rich imagery, Marquez weaves a tale of love, war, and political upheaval in Latin America. With its lush prose and masterful storytelling, One Hundred Years of Solitude is a landmark of Latin American literature." ,image="https://target.scene7.com/is/image/Target/GUEST_d9d0b738-42fb-4835-8287-f17ab5bc215d?wid=488&hei=488&fmt=pjpeg")

    book7 = Book(name = "The Hobbit", author = "J.R.R. Tolkien", genre = "High Fantasy", publishDate = "1937", link="https://www.amazon.com/The-Hobbit/dp/B08C8XFQMN/ref=sr_1_1?crid=2AM7FAYNMWSMA&keywords=the+hobbit+book&qid=1681233922&s=books&sprefix=the+hobbit+book%2Cstripbooks%2C78&sr=1-1",summary="This beloved children's book tells the story of Bilbo Baggins, a hobbit who embarks on a quest to reclaim a treasure hoard from the dragon Smaug. Along the way, he meets a host of memorable characters, including the wizard Gandalf and a band of dwarves. With its whimsical tone and imaginative world-building, The Hobbit is a timeless classic of fantasy literature." ,image="https://images.booksense.com/images/683/339/9780345339683.jpg")

    book8 = Book(name = "The Diary of a Young Girl", author = "Anne Frank", genre = "Autobiographical Novel", publishDate = "1947",link="https://www.amazon.com/Anne-Frank-Diary-Young-Definitive/dp/B003NYOBPA/ref=sr_1_2?crid=3F7XZ3Z0ERP1K&keywords=the+diary+of+a+young+girl+book&qid=1681233960&s=audible&sprefix=the+diary+of+a+young+girl+book%2Caudible%2C118&sr=1-2",summary="This powerful memoir documents the experiences of Anne Frank, a Jewish girl living in hiding in Amsterdam during the Nazi occupation of World War II. Through her candid and poignant reflections, readers gain insight into the daily struggles and fears of those living under persecution. With its messages of hope and resilience, The Diary of a Young Girl remains a testament to the human spirit in times of darkness." ,image="https://m.media-amazon.com/images/I/51pFO9wuBCL._AC_UF1000,1000_QL80_.jpg")

    book9 = Book(name = "The Lord of the Rings", author = "J.R.R. Tolkien", genre = "High Fantasy", publishDate = "1954-55",link="https://www.amazon.com/Two-Towers-Lord-Rings-Book/dp/B099NZM5S3/ref=sr_1_2?crid=1WISLWYI9F6LF&keywords=the+lord+of+the+ring+book&qid=1681234001&s=audible&sprefix=the+lord+of+the+ring+book%2Caudible%2C116&sr=1-2",summary="This epic trilogy follows the journey of Frodo Baggins, a hobbit tasked with destroying the powerful and corrupting One Ring. Along with his companions, including the wise wizard Gandalf and the loyal Samwise Gamgee, Frodo faces countless challenges and battles against the forces of evil. With its rich mythology and detailed world-building, The Lord of the Rings is a masterwork of high fantasy." ,image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1566425108l/33.jpg")

    book10 = Book(name = "The Adventures of Huckleberry Finn", author = "Mark Twain", genre = "Bildungsroman", publishDate = "1884",link="https://www.amazon.com/The-Adventures-of-Huckleberry-Finn/dp/B07W85TDQN/ref=sr_1_4?crid=1IVLWFFRFFVZ&keywords=huckleberry+finn+book&qid=1681234026&s=audible&sprefix=huckleberry+finnbook%2Caudible%2C72&sr=1-4",summary="This classic novel follows the misadventures of Huck Finn, a young boy from the American South, and his friend Jim, a runaway slave. Through their journey down the Mississippi River, Twain explores themes of race, identity, and freedom. With its use of vernacular language and biting satire, The Adventures of Huckleberry Finn remains a landmark of American literature." ,image="https://images.ucpress.edu/covers/isbn13/9780520343641.jpg")


    books = [book1,book2,book3,book4,book5,book6,book7,book8,book9,book10]

    print("Creating Quotes...")
    quote1 = Quote(quote = "Freedom is the freedom to say that two plus two make four. If that is granted, all else follows.", book = book1)
    quote2 = Quote(quote = "You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.", book = book2)
    quote3 = Quote(quote = "What really knocks me out is a book that, when you're all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it.", book = book3)
    quote4 = Quote(quote = "I hope she'll be a fool - that's the best thing a girl can be in this world, a beautiful little fool.", book = book4)
    quote5 = Quote(quote = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", book = book5)
    quote6 = Quote(quote = "Many years later, as he faced the firing squad, Colonel Aureliano Buendia was to remember that distant afternoon when his father took him to discover ice.", book = book6)
    quote7 = Quote(quote = "I know what you are thinking, and I do not approve.", book = book7)
    quote8 = Quote(quote = "In spite of everything, I still believe that people are really good at heart.", book = book8)
    quote9 = Quote(quote = "All we have to decide is what to do with the time that is given us.", book = book9)
    quote10 = Quote(quote = "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly.", book = book10)

    quotes = [quote1,quote2,quote3,quote4,quote5,quote6,quote7,quote8,quote9,quote10]

    print("Creating Reviews...")

    rev1 = Review( review = "This book is a warning about the dangers of totalitarianism, and it's more relevant today than ever. The vivid descriptions of the oppressive government and the protagonist's struggle to maintain his individuality are haunting and thought-provoking." ,user= user1, book= book1)

    rev2 = Review( review = "1984 is a masterpiece of dystopian fiction. Orwell's writing is precise and powerful, and the story's exploration of the relationship between language and power is still relevant today. A must-read for anyone interested in politics, philosophy, or science fiction.", user = user2, book= book1)

    rev3 = Review( review = "To Kill a Mockingbird is a classic for a reason. The story of Scout's coming of age and her father's struggle for justice in the face of racism is beautifully written and deeply moving. This book is a must-read for anyone who cares about social justice." , user= user3, book= book2)

    rev4 = Review( review = "I can't recommend this book enough. The characters are so well-drawn, and the story is both heartwarming and heart-wrenching. Lee's writing is stunningly beautiful, and her exploration of the complexities of race and class is still relevant today.", user= user4, book= book2)

    rev5 = Review( review = "The Catcher in the Rye is a classic bildungsroman that explores the angst and alienation of adolescence. Holden Caulfield is an unforgettable protagonist, and Salinger's writing captures the feeling of being a teenager like no other book I've read.",  user= user5, book= book3)

    rev6 = Review( review = "This book is a masterpiece of modern literature. The language is spare and precise, and Salinger's portrayal of Holden's struggles with depression and disillusionment is both honest and compassionate. Highly recommended.", user= user6, book= book3)

    rev7 = Review( review = "The Great Gatsby is a timeless classic that captures the decadence and excess of the Jazz Age. Fitzgerald's writing is lush and beautiful, and his characters are complex and flawed. This is a book that rewards multiple readings.", user= user1, book=book4 )

    rev8 = Review( review = "Fitzgerald's prose is simply breathtaking. The story of Gatsby's doomed love for Daisy is both tragic and beautiful, and the book's exploration of the American Dream still resonates today. A must-read for anyone who loves great literature.", user= user2, book= book4)

    rev9 = Review( review = "Pride and Prejudice is a classic of English literature, and for good reason. Austen's writing is witty and charming, and her exploration of the social mores of her time is both insightful and entertaining. This is a book that will never go out of style.", user= user3, book= book5)

    rev10 = Review( review = "Austen's characters are so well-drawn that they feel like real people. The story of Elizabeth Bennet's journey from prejudice to love is both delightful and thought-provoking, and the book's portrayal of the nuances of social class is still relevant today.", user= user4, book=book5)

    rev11= Review( review = "This book is a masterpiece of magical realism. García Márquez's prose is so rich and vivid that it feels like you're living in the world he's created. The story of the Buendía family is both epic and intimate, and the book's exploration of the cyclical nature of history is profound." ,user= user5, book= book6)

    rev12= Review( review = "One Hundred Years of Solitude is one of the most beautiful books I've ever read. García Márquez's writing is both lyrical and down-to-earth, and the story's mix of magical and mundane is both enchanting and unsettling. A must-read for anyone who loves great literature.", user= user6, book= book6)

    rev13= Review( review = "The Hobbit is a timeless classic that introduced the world to Middle-earth. Tolkien's world-building is incredible, and his characters are so well-drawn that they feel like old friends. This is a book that you'll want to revisit again and again.", user= user1, book= book7)

    rev14= Review( review = "Tolkien's writing is simply enchanting. The story of Bilbo Baggins's journey from comfort to adventure is both heartwarming and exciting, and the book's themes of bravery and loyalty are still relevant today.", user= user2, book= book7)

    rev15= Review( review = "The Lord of the Rings is an epic masterpiece that set the standard for modern fantasy. Tolkien's world-building is unparalleled, and his characters are so vividly drawn that they feel like real people. This is a book that will transport you to another world.", user= user3, book= book8)

    rev16= Review( review = "The Lord of the Rings is a classic for a reason. Tolkien's writing is so immersive that you'll forget you're reading a book. The story of Frodo's quest to destroy the One Ring is both thrilling and deeply moving, and the book's exploration of the nature of power is still relevant today.", user= user4, book= book8)

    rev17= Review( review = "The Chronicles of Narnia is a beloved classic that captures the imagination of readers young and old. Lewis's world-building is enchanting, and his characters are so memorable that they feel like friends. This is a series that you'll want to share with everyone you know." ,user= user5, book= book9)

    rev18= Review( review = "Lewis's writing is both charming and profound. The story of the Pevensie children's adventures in Narnia is both exciting and thought-provoking, and the books' exploration of faith and morality is still relevant today.", user= user6 , book= book9)

    rev19 = Review( review = "Animal Farm is a powerful allegory that exposes the dangers of totalitarianism. Orwell's writing is sharp and incisive, and his portrayal of the animals' struggle for freedom is both tragic and inspiring. This is a book that everyone should read." ,user= user1, book= book10)

    rev20 = Review( review = "Orwell's storytelling is both clever and devastating. The story of the animals' rebellion against their human oppressors is both entertaining and thought-provoking, and the book's exploration of power and corruption is still relevant today.", user= user2, book= book10)


    reviews = [rev1, rev2, rev3, rev4, rev5, rev6, rev7, rev8, rev9, rev10, rev11, rev12, rev13, rev14, rev15, rev16, rev17, rev18, rev19, rev20]

    # db.session.add_all(users)
    db.session.add_all(books)
    db.session.add_all(quotes)
    db.session.add_all(reviews)
    db.session.commit()

    print("Seeding done!...")

