{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "79492bae",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_18064/4033962591.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\Aarjav\\AppData\\Local\\Temp/ipykernel_18064/4033962591.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    pip install streamlit\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas_datareader as data\n",
    "from keras.models import load_model\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "start = '2010-01-01'\n",
    "end   = '2022-01-01'\n",
    "\n",
    "st.title('Stock Prediction')\n",
    "\n",
    "user_input = st.text_input('Enter Stock Ticker','TRIDENT.NS')\n",
    "df = data.DataReader(user_input,'yahoo',start,end)\n",
    "\n",
    "st.subheader('Data from 2010-2022')\n",
    "st.write(df.describe())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b5258e7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
