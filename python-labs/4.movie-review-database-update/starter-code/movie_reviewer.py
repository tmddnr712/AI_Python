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

# Rating
# NC-17(No Children) : 17 or older (17세 이하 미성년자 관람불가)
# R(Restricted) : Under 17 Requires Accompanying Parent or Adult Guardian (제한조건부 허가 : 17세 이하는 부모나 성인보호자 동반시 관람가)
# PG(Parental Guidance Suggested) : 보호자의 지도 필요, 연령제한은 없으나 부모나 보호자의 지도가 요구되는 영화
# * PG-13(Parental Guidance-13), Parents Strongly Cautioned (보호자의 엄격한 지도 필요)
# G(General Audiences) : 일반용, '연소자 관람가' 영화로 연령에 제한 없이 누구나 관람할 수 있는(All ages admitted)

inside_movie = {
    "title": "Inside Out",
    "genre": "Comedy",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

inception_movie = {
    "title" : "Inception",
    "genre": "Action",
    "id": "tt1375666",
    "year_released": 2010,
    "rating": "R",
    "score": 8.8,
    "out_of": 10,
    "reviews": 1984459
}

darknight_movie = {
    "title" : "The Dark Knight",
    "genre": "Action",
    "id": "tt0468569",
    "year_released": 2008,
    "rating": "R",
    "score": 9.0,
    "out_of": 10,
    "reviews": 1984459
}

# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/

print(inside_movie)
print(inception_movie)
print(darknight_movie)