# school_data.py
# Strahinja Radakovic
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import math
import pandas
import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022, school_data

# Declare any global variables needed to store the data here

#reshaping the school_data (my creation) array into a 2D array containing groups of school names and IDs
shaped_school_data = np.array(school_data.reshape(20,2))

#creating a large 3D array that sorts by year, school, and grade.
shaped_array = np.array([year_2013.reshape(20,3), year_2014.reshape(20,3), 
                         year_2015.reshape(20,3), year_2016.reshape(20,3), 
                         year_2017.reshape(20,3), year_2018.reshape(20,3), 
                         year_2019.reshape(20,3), year_2020.reshape(20,3), 
                         year_2021.reshape(20,3), year_2022.reshape(20,3)])

#creating a copy of the above array with all "NaN" values removed. Used for some calculations.
shaped_array_no_nan = shaped_array[~np.isnan(shaped_array)]




# You may add your own additional classes, functions, variables, etc.

#function that prints the school name and school code given a school_index input.
def school_name_ID(school_index):
    print("School Name: ", shaped_school_data[school_index][0], ",School Code: ", shaped_school_data[school_index][1])

#function that prints the mean enrollment for a given grade and school.
def mean_enrollment(school_index, grade):
    grade_index = grade - 10 #converts the grade input into an index that can be used to search through an array
    mean_enrollment_grade = int(np.mean(shaped_array[:,(school_index):(school_index+1),grade_index:grade_index+1]))
    print("Mean enrollmetn for Grade ", grade, ":", mean_enrollment_grade) #print statement

#function that prints the maximum enrollment at a given school over the 10 year data frame. Takes school_index as an argument.
def max_enrollment(school_index):
    enrollment_array = (shaped_array[:,(school_index):(school_index+1), :]) #creates an array with a given school's enrollment data
    maximum_enrollment = int(np.max(enrollment_array)) #calculates the maximum value in enrollment_array
    print("Highest enrollment for a single grade:", maximum_enrollment) #print statement

#function that prints minimum enrollment at a given school over the 10 year data frame. Works same as the function above, but uses np.min instead of np.max
def min_enrollment(school_index):
    enrollment_array = (shaped_array[:,(school_index):(school_index+1), :])
    minimum_enrollment = int(np.min(enrollment_array))
    print("Highest enrollment for a single grade:", minimum_enrollment)

#function that prints the total enrollment at a school for a given year. Takes year and school_index as arguments.
def total_enrollment(year, school_index): 
    year_indexed = year - 2013 #converts a year input into a year index which can be used to search through an array.
    total_enrollment_array = shaped_array[year_indexed:year_indexed+1, (school_index):(school_index+1), :] #creates a new array that corresponds with all enrollments at a school for a given year.
    total_enrollment_sum = int(np.sum(total_enrollment_array)) #sums up all enrollments in a given year at a given school.
    print("Total enrollment for ", year, ":", total_enrollment_sum) #print statement

#function that prints the total enrollment at a given school over the 10 years of given data. Takes school as input
def total_enrollment_10_yrs(school_index): 
    total_10yr_enrollment_array = shaped_array[:, (school_index):(school_index+1), :] #creates an array that contains all enrollments over 10 years at a given school.
    total_10yr_enrollment = int(np.sum(total_10yr_enrollment_array)) #adds up all enrollments over the 10 years.
    print("Total ten year enrollment:", total_10yr_enrollment) #print statement

#function that prints the mean enrollment over 10 years for a given school. Takes school as input
def mean_total_enrollment_over10yrs(school_index):
    total_10yr_enrollment_array = shaped_array[:, (school_index):(school_index+1), :] #creates an array that contains all enrollments over 10 years at a given school.
    mean_10yr_enrollment_10yrs = int(np.sum(total_10yr_enrollment_array)/10) #adds up all enrollments over the 10 years, and divides them by 10 to get the mean.
    print("Mean total enrollment over ten years:", mean_10yr_enrollment_10yrs) #print statement

#function that prints the median enrollment at a school given the enrollment is greater than 500.
def median_enrollments_over500(school_index):
    enrollment_array = (shaped_array[:,(school_index):(school_index+1), :]) #creates an array with a given school's enrollment data
    all_enrollemnts_over_500 = enrollment_array[enrollment_array > 500] #filters out all enrollments less than and equal to 500 from the enrollment array
    median = int(np.median(all_enrollemnts_over_500)) #finds the median enrollment
    print("For all enrollments over 500, the median value was:", median) #print statement

#function that prints the mean enrollment at all schools in a given year.
def all_schools_mean_enrl_year(year):
    year_indexed = year - 2013 #converts a year input into a year index which can be used to search through an array.
    mean_enrollment_allschools_array = shaped_array[year_indexed:year_indexed+1, :, :] #created an array with all enrollments in all schools for a given year.
    mean_enrollment_allschools_array = mean_enrollment_allschools_array[~np.isnan(mean_enrollment_allschools_array)] #removes NaN values from array
    mean_enrollment_allschools = int(np.mean(mean_enrollment_allschools_array)) #calculates the mean
    print("Mean enrollment in ", year, ":", mean_enrollment_allschools) #print statement

#function that prints the total graduating class in a year.
def total_graduating_class(year):
    year_indexed = year - 2013 #converts a year input into a year index which can be used to search through an array.
    total_graduating_class_array = shaped_array[year_indexed:year+1, :, 2:3] #creates an array that contains all grade 12s for all schools in a given year
    total_graduating_class_array = total_graduating_class_array[total_graduating_class_array > 0] # getting rid of NaN
    total_graduating_class = int(np.sum(total_graduating_class_array)) #summing up all grade 12s
    print("Total graduating class of", year, ":", total_graduating_class) #print statement

#function that prints the highest enrollment in the 10 years of given data
def highest_enrollment_single_grade():
    highest_enrollment = int(np.max(shaped_array_no_nan)) #finds highest value in all enrollments.
    print("Highest enrollment for a single grade:", highest_enrollment) #print statement

#function that prints the lowest enrollment in the 10 years of given data
def lowest_enrollment_single_grade():
    lowest_enrollment = int(np.min(shaped_array_no_nan)) #finds lowest value in all enrollments.
    print("Lowest enrollment for a single grade:", lowest_enrollment) #print statement


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    
    #print(shaped_array)
    print("Shape of full data array: ", shaped_array.shape) #print the shape of data array
    print("Dimensions of full data array: ", shaped_array.ndim) #print the dimension of the data array

    # Prompt for user input
    school_selection = input("Please enter the high school name or school code:")
    if(np.isin(school_selection,np.ndarray.flatten(school_data))): #checks if user input is valid.
        index_of_school = int(np.where(shaped_school_data == school_selection)[0][0]) #if the user input is valid, assign input to the index_of_school
    else: 
        raise ValueError('You must enter a valid school name or code.') #raise ValueError if input is invalid
    

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    #school name and ID print
    school_name_ID(index_of_school)

    #mean enrollment for a given grade
    mean_enrollment(index_of_school, 10)
    mean_enrollment(index_of_school, 11)
    mean_enrollment(index_of_school, 12)

    #maximum & minimum enrollment
    max_enrollment(index_of_school)
    min_enrollment(index_of_school)

    #total enrollment for a given year
    total_enrollment(2013, index_of_school)
    total_enrollment(2014, index_of_school)
    total_enrollment(2015, index_of_school)
    total_enrollment(2016, index_of_school)
    total_enrollment(2017, index_of_school)
    total_enrollment(2018, index_of_school)
    total_enrollment(2019, index_of_school)
    total_enrollment(2020, index_of_school)
    total_enrollment(2021, index_of_school)
    total_enrollment(2022, index_of_school)

    #total 10 year enrollment
    total_enrollment_10_yrs(index_of_school)

    #mean total enrollemtn over 10 years
    mean_total_enrollment_over10yrs(index_of_school)

    #for all enrollments over 500, median enrollment
    median_enrollments_over500(index_of_school)
    

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    #mean enrollment in a year (all schools) proof
    all_schools_mean_enrl_year(2013)
    all_schools_mean_enrl_year(2022)

    #total graduating class of given year
    total_graduating_class(2022)

    #highest and lowest enrollment for a single grade, all schools
    highest_enrollment_single_grade()
    lowest_enrollment_single_grade()




if __name__ == '__main__':
    main()

