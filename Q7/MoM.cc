#include<bits/stdc++.h>
using namespace std;

// all position should be given according to zero indexed array
int give_median(vector<int>& arr, int initial, int final)
{
    sort(arr.begin()+initial,arr.begin()+final);
    int mid = (initial + final) / 2;
    return arr[mid];
}

//give arr_size as sizeof(arr)/sizeof(int)
int median_of_median(vector<int>& arr, int arr_size, int divide_size)
{
    if (arr_size < divide_size)
    {
        int median = give_median(arr, 0, arr_size - 1);
        return median;
    }

    int no_full_group = arr_size / divide_size;
    int elements_in_last = arr_size % divide_size;

    int next_arr_size;

    if (elements_in_last == 0)
        next_arr_size = no_full_group;
    else
        next_arr_size = no_full_group + 1;

    vector<int> next_arr(next_arr_size);

    for (int i = 0; i < next_arr_size; i++)
    {
        if (i == arr_size)
            next_arr[i] = give_median(arr, divide_size * i, arr_size - 1);
        else
            next_arr[i] = give_median(arr, divide_size * i, divide_size * (i + 1) - 1);
    }

    return median_of_median(next_arr, next_arr_size, divide_size);
}

int main()
{
    srand(time(0));

    int arr_size = 10;

    vector<int> arr(arr_size);

    for (int i = 0; i < arr_size; i++)
        arr[i] = rand() % 100;

    for (int i = 0; i < arr_size; i++)
        printf("%d ", arr[i]);
    printf("\n");

    vector<int> copy = arr;

    printf("Median of Medians: %d\n", median_of_median(arr, arr_size, 5));
    printf("Direct: %d\n", give_median(copy, 0, arr_size - 1));

    return 0;
}