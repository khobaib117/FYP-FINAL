const express = require("express");
const mongoose = require("mongoose");
const env = require("dotenv");

const app = express();
const productRoutes = require("./routes/product");
const userRoutes = require("./routes/auth");
const wishlistRoutes = require("./routes/wishlist");
const wardrobeRoutes = require("./routes/wardrobe");
const prelovedRoutes = require("./routes/prelovedItems");


var cors = require('cors')

app.use(cors()) // Use this after the variable declaration
//Environment variable or constants
env.config();

// Database connection
const connectDB = async () => {
  try {
    await mongoose
      .connect(
        `mongodb://${process.env.MONGO_DB_USER}:${process.env.MONGO_DB_PASSWORD}@cluster0-shard-00-00.4s7gf.mongodb.net:27017,cluster0-shard-00-01.4s7gf.mongodb.net:27017,cluster0-shard-00-02.4s7gf.mongodb.net:27017/${process.env.MONGO_DB_DATABASE}?ssl=true&replicaSet=atlas-ucptyb-shard-0&authSource=admin&retryWrites=true&w=majority`,
        {
          useNewUrlParser: true,
          useUnifiedTopology: true,
          useCreateIndex: true,
          useFindAndModify: false,
        }
      )
      .then(() => {
        console.log("MongoDB Connected");
      });
  } catch (err) {
    console.error(err.message);
    // exit process with failure
    process.exit(1);
  }
};

connectDB();

app.use(express.json());
app.use(express.static(__dirname+"/uploads"));
app.use("/api", productRoutes);
app.use("/api", userRoutes);
app.use("/api", wishlistRoutes);
app.use("/api", wardrobeRoutes);
app.use("/api", prelovedRoutes);

// Listen for requests
app.listen(process.env.PORT, () => {
  console.log(`Server is running on port ${process.env.PORT}`);
});
