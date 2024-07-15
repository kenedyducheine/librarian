
### Lib 2023 
Using a Random Forest Classifier model to predict which books from the NYT Best Seller list (2009 - 2019) I would enjoy based on ratings I had given previous books. I used Goodreads to consolidate my book reviews. The synopsis of the books, as vector embeddings, and my review, were the training features. 

Cannot scale up given that Goodreads API no longer exists. 

#### Considerations 
1. I joined Goodreads in January 2023, so my 'read' column does not contain enough books for training. Used all bookshelves (read + want to read) as training data. Additionally, I randomized my reviews of these books because I am quite liberal with my ratings. I wanted to train the model as if I were a more critical reader and suggest books from there.
2. Training data is very small because I can only read so many books in a year. Testing data does not encompass all of the NYT books (60k >) because I used subscription API to pull the synopsis and could only do 5k a day. 

#### Updates
1. Decided to use Bert Embeddings instead of OpenAI because bert is a bidirectional encoder (OpenAI is bidirectional).
2. Randomized my reviews for better performance

#### Frameworks used 
1. HuggingFace Bert
2. TensorFlow (initially, but switched because of data size)
3. SciKit Learn 
