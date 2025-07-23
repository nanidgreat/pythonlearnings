{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP6JXPFeBxb50ZxDk0HhOno",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nanidgreat/pythonlearnings/blob/main/basics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. All about print function\n",
        "*   Multiple strings can be seperated by comma(,) to print them\n",
        "*   All types data types be printed with separted by command\n",
        "*   Each item to be printed can be separted by 'sep=\"\" ' parameter in print\n",
        "*   'end=\"\" ' parameter can be used to change the end of the string to be printed\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "SDqILb9DIObx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello\",\"how are you\")\n",
        "print(\"hello\",True,5,3.14)\n",
        "print(\"hello\",True,5,3.14,sep=\"-\")\n",
        "print(\"hello\",True,5,3.14,end=\"/\")\n",
        "print(\"I am\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vz2246JdIS7h",
        "outputId": "408b6bd6-69d8-49a5-f0bf-bfd1ad1bdeb4"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello how are you\n",
            "hello True 5 3.14\n",
            "hello-True-5-3.14\n",
            "hello True 5 3.14/I am\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Data types in Python\n",
        "There are 3 types of Data types in python.They are\n",
        "*   Basic types(Integer,float,complex,boolean,string)\n",
        "*   container types(List,tuple,set,dictonary)\n",
        "*   user defined types(class)\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "E163-brPJojT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#integer\n",
        "print(4)\n",
        "print(500000000000000000000000000000000000000000000000000000000000000000)\n",
        "print(1e308) # i.e 10^308 so this the max integer number which can be printed\n",
        "print(1e309) #10^309\n",
        "#float\n",
        "print(1.4)\n",
        "print(1.7e308) # max float number\n",
        "print(1.7e309)\n",
        "#boolean\n",
        "print(True,False)\n",
        "#complex\n",
        "print(4+3j)\n",
        "#string\n",
        "print('hello',\"hello\",\"\"\"hello how are u\"\"\",sep=\"-\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IMIGmy1wLZ5M",
        "outputId": "fadbc3a2-2947-4dbb-fb6f-3ae9c62b57e5"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "500000000000000000000000000000000000000000000000000000000000000000\n",
            "1e+308\n",
            "inf\n",
            "1.4\n",
            "1.7e+308\n",
            "inf\n",
            "True False\n",
            "(4+3j)\n",
            "hello-hello-hello how are u\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#list\n",
        "print([1,2,3,5,\"hello\",1.4,True,1])\n",
        "#Tuple\n",
        "print((1,2,3,5,\"hello\",1.4,True,1))\n",
        "#set\n",
        "print({6,2,3,5,\"hello\",1.4,True,2})\n",
        "#dictionary\n",
        "print({1:\"hello\",2:True,3:234,4:1.7})"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "30aaPhXwM3Lu",
        "outputId": "4c28f26a-7d45-4d25-cd54-66e6f43524ae"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 5, 'hello', 1.4, True, 1]\n",
            "(1, 2, 3, 5, 'hello', 1.4, True, 1)\n",
            "{1.4, 2, 3, True, 5, 6, 'hello'}\n",
            "{1: 'hello', 2: True, 3: 234, 4: 1.7}\n"
          ]
        }
      ]
    }
  ]
}