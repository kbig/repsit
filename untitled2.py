import os
#from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
image_dir = "C:/Users/Yun/Desktop/dataset"
image_width = 176
image_height = 208
training_epochs = 15
batch_size = 100
image_list = os.listdir(image_dir)



for i in range(len(image_list)):
    image_list[i] = image_dir + image_list[i]


label_dir = "/home/chanwoo/Sources/Temp_data_Set/DataSet/label_csv/Label.csv"
label_list = [label_dir]

imagename_queue = tf.train.string_input_producer(image_list)
labelname_queue = tf.train.string_input_producer(label_list)

image_reader = tf.WholeFileReader()
label_reader = tf.TextLineReader()

image_key, image_value = image_reader.read(imagename_queue)
label_key, label_value = label_reader.read(labelname_queue)

image_decoded = tf.cast(tf.image.decode_jpeg(image_value, channels=1), tf.float32)
label_decoded = tf.cast(tf.decode_csv(label_value, record_defaults=[[0]]), tf.float32)

label = tf.reshape(label_decoded, [1])
image = tf.reshape(image_decoded, [-1, image_width, image_height, 1])


W1 = tf.Variable(tf.random_normal([5, 5, 1, 32], stddev=0.01))
L1 = tf.nn.conv2d(image, W1, strides=[1, 2, 2, 1], padding='SAME')
L1 = tf.nn.relu(L1)

L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[
                        1, 2, 2, 1], padding='SAME')
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1],
                    strides=[1, 2, 2, 1], padding='SAME')

L2_flat = tf.reshape(L2, [-1, 22 * 26 * 64])
W3 = tf.get_variable("W3", shape=[22 * 26 * 64, 3],
                     initializer=tf.contrib.layers.xavier_initializer())

b = tf.Variable(tf.random_normal([3]))
logits = tf.matmul(L2_flat, W3) + b
Y=1
learning_rate = 0.001
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())

print(L2)
print('Learning started. It takes sometime.')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={
      X: mnist.test.images, Y: mnist.test.labels}))

# Get one and predict
r = random.randint(0, mnist.test.num_examples - 1)
print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("Prediction: ", sess.run(
    tf.argmax(logits, 1), feed_dict={X: mnist.test.images[r:r + 1]}))


  