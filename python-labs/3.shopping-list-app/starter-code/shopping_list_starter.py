#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = input("Enter your choice [a|b|c|d|e]:")

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
    if choice == "a":
        print("쇼핑이 끝나면 '끝'을 입력해 주세요.")
        while True:
            items = []
            items = input("쇼핑 아이템을 입력하세요: ")
            if items != "끝":
                shopping_list.append(items)
            elif items == "끝":
                print("아이템이 입력 되었습니다.")
                print(shopping_list)
                break

    if choice == "b":
        print(shopping_list)
        print("버릴 품목을 다 입력하시면 '끝'을 입력해주세요.")
        while True:
            drop_items = input("버릴 품목을 입력해주세요: ")
            if drop_items in shopping_list:
                shopping_list.remove(drop_items)
                print(shopping_list)
            elif drop_items == "끝":
                print("품목을 지웠습니다.")
                print(shopping_list)
                break

    if choice == "c":
        print("품목 확인")
        print("확인을 다 하셨으면 '끝'을 입력해주세요.")
        while True:
            check_items = input("확인하고 싶은 품목을 입력하세요:")
            if check_items in shopping_list:
                print(check_items + "가 쇼핑리스트 안에 있습니다.")
            elif check_items not in shopping_list:
                print(check_items + "품목이 쇼핑리스트 안에 없습니다.")
                break


    if choice == "d":
        print(shopping_list)


    if choice == "e":
        print("EXIT")
        break
