"""Merge‑sort based inversion counting with a clean class interface.

The algorithm recursively splits the input list, counts inversions in each half
and during the merge step counts cross‑inversions. The public method ``count``
accepts any iterable of comparable items and returns the total inversion count.
"""

from __future__ import annotations

from typing import List, Sequence, Tuple


class InversionCounter:
    """Encapsulate the inversion counting logic.

    Attributes
    ----------
    _data: List[int]
        The list to be processed; stored as a mutable copy.
    """

    def __init__(self, data: Sequence[int]):
        self._data = list(data)

    def count(self) -> int:
        """Return the number of inversions in ``self._data``.

        Returns
        -------
        int
            Total inversions found.
        """
        _, inv = self._merge_sort(self._data)
        return inv

    def _merge_sort(self, arr: List[int]) -> Tuple[List[int], int]:
        """Recursive merge‑sort that also returns inversion count.

        Parameters
        ----------
        arr: List[int]
            Sub‑array to sort.

        Returns
        -------
        Tuple[List[int], int]
            Sorted sub‑array and the number of inversions inside it.
        """
        n = len(arr)
        if n <= 1:
            return arr[:], 0
        mid = n // 2
        left, inv_left = self._merge_sort(arr[:mid])
        right, inv_right = self._merge_sort(arr[mid:])
        merged, inv_merge = self._merge(left, right)
        return merged, inv_left + inv_right + inv_merge

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> Tuple[List[int], int]:
        """Merge two sorted lists counting cross‑inversions.

        Parameters
        ----------
        left, right: List[int]
            Sorted halves.

        Returns
        -------
        Tuple[List[int], int]
            Merged list and cross‑inversion count.
        """
        i = j = 0
        merged: List[int] = []
        inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # All remaining elements in left are greater than right[j]
                inv_count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count
